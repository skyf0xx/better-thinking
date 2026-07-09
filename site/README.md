# site/

The Better Thinking homepage, published to [zenbin.org](https://zenbin.org) at
**https://zenbin.org/p/better-thinking**.

## Files

- `index.html` — the full homepage. Edit this directly; it's a standalone file (inline CSS, no build step).
- `publish.mjs` — publishes `index.html` to zenbin.org.
- `.zenbin/key.json` — the Ed25519 keypair that owns the `better-thinking` page on zenbin.org. **Gitignored, never commit it.** Whoever holds this key can update the live page.

## Publishing changes

After editing `index.html`:

```
node site/publish.mjs
```

First run (no `site/.zenbin/key.json` present) generates a new Ed25519 keypair, registers it with zenbin.org, and publishes. Every run after that reuses the same key and re-publishes to the same page, since zenbin.org pages are owned by whichever key created them.

If `site/.zenbin/key.json` is ever lost, running the script again will register a **new** key and publish under a **new** page id ownership — it can no longer update the existing `https://zenbin.org/p/better-thinking` page. Back the key up somewhere safe (password manager, not git) if that matters to you.
