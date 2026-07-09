#!/usr/bin/env node
// Publishes site/index.html to zenbin.org as a signed page.
//
// Usage:
//   node site/publish.mjs                 # register a key on first run, then publish
//
// The keypair is stored at site/.zenbin/key.json (gitignored). Re-running this
// script reuses the same key and re-publishes to the same page id, so the
// owning key can update the page later.

import { generateKeyPairSync, createPrivateKey, createHash, sign, randomBytes } from 'node:crypto';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const KEY_DIR = join(__dirname, '.zenbin');
const KEY_FILE = join(KEY_DIR, 'key.json');
const PAGE_ID = 'better-thinking';
const HTML_FILE = join(__dirname, 'index.html');
const TITLE = 'Better Thinking — a library of thinking procedures for Claude Code';

async function ensureKey() {
  if (existsSync(KEY_FILE)) {
    return JSON.parse(readFileSync(KEY_FILE, 'utf8'));
  }

  mkdirSync(KEY_DIR, { recursive: true });
  const { publicKey, privateKey } = generateKeyPairSync('ed25519');
  const jwkPub = publicKey.export({ format: 'jwk' });
  const jwkPriv = privateKey.export({ format: 'jwk' });
  const keyId = `better-thinking-site-${Date.now()}`;

  const res = await fetch('https://zenbin.org/v1/keys/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      keyId,
      publicJwk: { crv: jwkPub.crv, kty: jwkPub.kty, x: jwkPub.x },
    }),
  });

  if (!res.ok) {
    throw new Error(`key registration failed: ${res.status} ${await res.text()}`);
  }

  const record = { keyId, jwkPub, jwkPriv };
  writeFileSync(KEY_FILE, JSON.stringify(record, null, 2));
  console.log(`registered new zenbin key: ${keyId}`);
  return record;
}

function sign_request(method, path, bodyBuf, jwkPriv) {
  const privateKey = createPrivateKey({ key: jwkPriv, format: 'jwk' });
  const digest = createHash('sha256').update(bodyBuf).digest('base64');
  const contentDigest = `sha-256=:${digest}:`;
  const timestamp = new Date().toISOString();
  const nonce = randomBytes(16).toString('hex');
  const canonical = [method, path, timestamp, nonce, contentDigest].join('\n');
  const signature = sign(null, Buffer.from(canonical), privateKey).toString('base64url');
  return { timestamp, nonce, contentDigest, signature };
}

async function publish() {
  const { keyId, jwkPriv } = await ensureKey();

  const html = readFileSync(HTML_FILE, 'utf8');
  const bodyStr = JSON.stringify({ html, title: TITLE });
  const bodyBuf = Buffer.from(bodyStr);

  const path = `/v1/pages/${PAGE_ID}`;
  const { timestamp, nonce, contentDigest, signature } = sign_request('POST', path, bodyBuf, jwkPriv);

  const res = await fetch(`https://zenbin.org${path}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Zenbin-Key-Id': keyId,
      'X-Zenbin-Timestamp': timestamp,
      'X-Zenbin-Nonce': nonce,
      'Content-Digest': contentDigest,
      'X-Zenbin-Signature': `:${signature}:`,
    },
    body: bodyBuf,
  });

  const result = await res.json();
  if (!res.ok) {
    throw new Error(`publish failed: ${res.status} ${JSON.stringify(result)}`);
  }

  console.log(`published: ${result.url}`);
}

publish().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
