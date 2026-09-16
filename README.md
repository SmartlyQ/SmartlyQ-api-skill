# SmartlyQ API skill

A [Claude Code](https://docs.claude.com/en/docs/claude-code) skill for building
against the [SmartlyQ REST API](https://docs.smartlyq.com): social publishing and
scheduling, AI content generation, SEO, paid ads reporting, WhatsApp, CRM and
automations.

It gives an agent the endpoint map, the scope model, the error semantics and the
async-job and webhook mechanics, so it writes working calls instead of inventing
plausible ones.

## Install

Copy the skill into your project or your personal skills directory:

```bash
git clone https://github.com/SmartlyQ/SmartlyQ-api-skill
mkdir -p ~/.claude/skills/smartlyq-api
cp -r SmartlyQ-api-skill/SKILL.md SmartlyQ-api-skill/references ~/.claude/skills/smartlyq-api/
```

Claude Code picks it up automatically when a task involves the SmartlyQ API.

## What's in it

| File | Contents |
| --- | --- |
| `SKILL.md` | How to choose an endpoint, the scope model, error handling, what needs a human's approval |
| `references/endpoints.md` | All 385 operations across 33 resource groups, generated from the published OpenAPI spec |
| `references/authentication.md` | Key types, the full scope list, common auth failures |
| `references/errors.md` | Status codes, error codes, what each one means |
| `references/rate-limiting.md` | Limits, headers, backoff |
| `references/async-jobs.md` | Job lifecycle and polling |
| `references/idempotency.md` | Safe retries on requests that spend credits |
| `references/webhooks.md` | Subscriptions, payloads, signature verification |

## Why a skill and not just the docs

The failure mode this prevents is an agent guessing. Without the endpoint map it
invents a path that looks right, gets a 404, and reports it as an outage.
Without the scope model it reads a `403` as an auth problem and retries forever.
Without the async-job contract it treats a `pending` status as a failure.

Everything here comes from the published documentation and the public OpenAPI
spec. It adds no access; it just stops the guessing.

## Requirements

A SmartlyQ account on a **Pro plan or higher** - API access is included from Pro
up. Create a key in the [Developer dashboard](https://app.smartlyq.com/next/developer).
Use a `sqk_test_*` key while developing: it charges no credits.

## Keeping it current

`references/endpoints.md` is generated from
<https://docs.smartlyq.com/openapi.json>, and the other reference files mirror
pages on <https://docs.smartlyq.com>. The docs are the source of truth. If a
file here disagrees with them, the docs win - please open an issue.

## Related

- [SmartlyQ/smartlyq-plugins](https://github.com/SmartlyQ/smartlyq-plugins) - Claude Code and Cursor plugins for the hosted MCP server, if you want the tools rather than the API
- [Official SDKs](https://docs.smartlyq.com) - Node, Python, PHP, Go, and a CLI
- Setup pages: [smartlyq.com/claude](https://smartlyq.com/claude) - [/codex](https://smartlyq.com/codex) - [/cursor](https://smartlyq.com/cursor) - [/vscode](https://smartlyq.com/vscode)

## License

[MIT](LICENSE)
