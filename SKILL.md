---
name: smartlyq-api
description: Build against the SmartlyQ REST API - social publishing and scheduling, AI content generation (articles, images, video, audio, presentations), SEO research and audits, paid ads reporting, WhatsApp, CRM and automations. Use when writing code that calls api.smartlyq.com, choosing an endpoint or scope, handling an async job or a webhook, or debugging a 401, 402, 403 or 429 from SmartlyQ.
---

# SmartlyQ REST API

Base URL: `https://api.smartlyq.com/v1`
Auth: `Authorization: Bearer sqk_live_...`

296 paths across 33 resource groups. The full map is in
[references/endpoints.md](references/endpoints.md); the published spec is at
<https://docs.smartlyq.com/openapi.json>.

## Before you write any request

**Find the endpoint, do not invent it.** Look it up in
[references/endpoints.md](references/endpoints.md). If the operation you want
is not there, it is not in the public API - say so instead of guessing a
plausible path. A guessed endpoint returns 404 and a guessed scope returns 403,
and both look like outages when reported carelessly.

**Get the request body from the spec, not from the summary line.** The endpoint
map gives you the method, path and a one-line summary. That is enough to choose
an endpoint and not enough to build a body. Fetch the operation from the
OpenAPI spec before constructing a payload.

**Prefer an official SDK over a hand-rolled client.** There are five, all
generated from the same spec and kept in step with it:
`@smartlyqofficial/node`, `smartlyq` (PyPI), `smartlyq/sdk` (Packagist),
`github.com/SmartlyQ/smartlyq-go`, and the `@smartlyqofficial/cli`.

## Authentication and scopes

Keys come from the [Developer dashboard](https://app.smartlyq.com/next/developer).
`sqk_live_*` is production and spends real credits; `sqk_test_*` is sandbox and
charges none.

Scopes are per-resource and per-verb: `social:read`, `social:write`,
`ads:read`, `seo:read`, `contacts:write`, and so on - see
[references/authentication.md](references/authentication.md) for the full list.

Two things that regularly cost people an afternoon:

- A key carries exactly the scopes ticked when it was created. Adding a scope
  later does **not** widen an existing key. Edit the key or mint a new one.
- `403 FORBIDDEN` means the key is valid and the scope is missing. It is not an
  auth failure and retrying will never fix it.

API access requires a **Pro plan or higher**. If every call returns a
permission error on a valid key, check the plan before debugging the code.

## Errors

Every error has the same shape:

```json
{ "success": false, "error": { "code": "ERROR_CODE", "message": "..." } }
```

The ones worth special handling:

| Status | Code | What to actually do |
| --- | --- | --- |
| 401 | `UNAUTHORIZED` | Key missing or invalid. Do not retry. |
| 402 | `INSUFFICIENT_CREDITS` | Wallet too low. Tell the user; do not retry. |
| 403 | `FORBIDDEN` | Key lacks the scope. Do not retry. |
| 403 | `CONNECTION_SCOPE_MISSING` | The **social account** is missing a permission, not the key. `details.reconnect_required` is true - the user must reconnect that account. |
| 409 | duplicate | Idempotency key replay. Treat as success. |
| 429 | `RATE_LIMITED` | Back off using `Retry-After`. |

Full list: [references/errors.md](references/errors.md).

## Rate limits

60 requests per minute by default, configurable per key. Every response carries
`X-RateLimit-Limit`, `X-RateLimit-Remaining` and `X-RateLimit-Reset`. On 429,
honour `Retry-After` rather than backing off on a guess.

## Async jobs

Article, video, image and presentation generation are asynchronous. They return
`202` with a `job_id`; poll `GET /jobs/{job_id}` every 3-5 seconds until
`status` is `completed` or `failed`.

Never block a user-facing request on a generation job, and never treat a
`pending` status as a failure. Details:
[references/async-jobs.md](references/async-jobs.md).

## Idempotency

Send an `Idempotency-Key` header on any POST that creates something or spends
credits. A replay returns the original result rather than doing the work twice.
This matters most on retries after a timeout, where the first request may well
have succeeded.

## Webhooks

Subscribe with the `webhooks` scope. Payloads are signed - verify the signature
before trusting the body, and return 2xx quickly, doing the real work out of
band. See [references/webhooks.md](references/webhooks.md).

## Working on someone's live account

These endpoints act on real accounts, real money and real audiences. Publishing
a post, launching or editing an ad campaign, sending a WhatsApp broadcast and
emailing a contact list are all irreversible from the API's point of view.

Show the user what you are about to do and wait for a yes. Where an endpoint can
schedule instead of publishing immediately, prefer scheduling when the user has
not said which they want. Use a `sqk_test_*` key while developing.
