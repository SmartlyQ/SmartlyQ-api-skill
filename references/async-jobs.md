<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;
     if this file and the docs disagree, the docs win. -->

# Async Jobs

> How long-running operations work with the job queue.

## Overview

Some API operations (article generation, video creation, image generation, presentation generation) are **asynchronous**. Instead of returning the result immediately, the API returns a `job_id` that you poll until the result is ready.

## Job lifecycle

```
POST /articles/generate
     │
     ▼
202 Accepted → { "job_id": "job_abc123", "status": "pending" }
     │
     ▼  (poll every 3-5 seconds)
GET /jobs/job_abc123
     │
     ├── { "status": "processing" }   ← still working
     ├── { "status": "completed", "result": { ... } }  ← done
     └── { "status": "failed", "error": { ... } }  ← error
```

## Polling for results

```bash
curl https://api.smartlyq.com/v1/jobs/job_abc123 \
  -H "Authorization: Bearer sqk_live_xxxxxxxxxxxx"
```

### Job statuses

| Status       | Meaning                                            |
| ------------ | -------------------------------------------------- |
| `pending`    | Queued, not yet started                            |
| `processing` | Actively running                                   |
| `completed`  | Done — `result` field contains the output          |
| `failed`     | Error — `error` field explains what went wrong     |
| `cancelled`  | Job was cancelled via `POST /jobs/{job_id}/cancel` |

## Webhooks (alternative)

Instead of polling, configure a [webhook](/guides/webhooks) to receive a notification when the job completes.
