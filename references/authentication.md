<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;
     if this file and the docs disagree, the docs win. -->

# Authentication

> How to authenticate requests to the SmartlyQ API.

All API requests require a **Bearer token** in the `Authorization` header.

## API keys

Get your API key from the [Developer Dashboard](https://app.smartlyq.com/next/developer).

| Key prefix   | Environment                          |
| ------------ | ------------------------------------ |
| `sqk_live_*` | Production — real credits, real data |
| `sqk_test_*` | Sandbox — no credits charged         |

## Making authenticated requests

Include your key in the `Authorization` header:

```bash
curl -X GET https://api.smartlyq.com/v1/me \
  -H "Authorization: Bearer sqk_live_xxxxxxxxxxxx"
```

<Warning>
  Never expose your API key in client-side code, public repositories, or logs.
</Warning>

## Scopes

Each key can be limited to specific scopes. Available scopes:

| Scope                                                      | Access                                                                                                            |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `articles:read`                                            | List and get articles                                                                                             |
| `articles:write`                                           | Generate and delete articles                                                                                      |
| `images:read` / `images:write`                             | Image generation and listing                                                                                      |
| `videos:read` / `videos:write`                             | Video generation and listing                                                                                      |
| `presentations:read`                                       | List and get presentations                                                                                        |
| `presentations:write`                                      | AI presentation generation                                                                                        |
| `social:read` / `social:write`                             | Social accounts, posts, queues, comments, DMs, reviews, validation, platform lookups                              |
| `audio:read` / `audio:write`                               | Text-to-speech, speech-to-text                                                                                    |
| `urls:read` / `urls:write`                                 | URL shortening                                                                                                    |
| `captain:use`                                              | AI Captain conversations                                                                                          |
| `chatbot:use`                                              | Chatbot management and messaging                                                                                  |
| `media:read` / `media:write`                               | Media library                                                                                                     |
| `analytics:read`                                           | Post, account, derived and inbox analytics                                                                        |
| `seo:read`                                                 | Keyword research, SERP, rank tracking, competitors, backlinks, on-page audits                                     |
| `contacts:read` / `contacts:write`                         | CRM contacts, their tags and notes, custom field definitions, the workspace tag vocabulary, automation enrollment |
| `companies:read` / `companies:write`                       | Companies / organisations, and linking contacts to them                                                           |
| `tasks:read` / `tasks:write`                               | CRM tasks and activities, and logging time against them                                                           |
| `calendar:read` / `calendar:write`                         | Booking pages and open slots; taking and cancelling bookings                                                      |
| `opportunities:read` / `opportunities:write`               | Pipelines and deals/opportunities, stage moves, status                                                            |
| `workspaces:read` / `workspaces:write` / `workspaces:bulk` | Workspaces, their subscriptions and wallets; bulk workspace actions                                               |
| `profiles:read` / `profiles:write` / `profiles:manage`     | Connection profiles, their accounts, and connect links                                                            |
| `webhooks:read` / `webhooks:write`                         | Webhook subscriptions, delivery logs, test and replay deliveries                                                  |
| `logs:read`                                                | Your API request and webhook delivery history (`GET /logs`)                                                       |
| `jobs:read`                                                | Async job status                                                                                                  |
| `ads:read` / `ads:write`                                   | Ad campaigns, ad sets, ads, audiences, pixels, lead forms, creatives, account diagnostics                         |

## Error responses

If your key is missing or invalid, the API returns:

* **401 Unauthorized** — missing or invalid key
* **403 Forbidden** — valid key but insufficient scope

```json
{
  "success": false,
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Missing or invalid API key."
  }
}
```
