# Notes

```text
Client --HTTP--> POST /v1/sessions
Client --WS----> /v1/sessions/{id}/ws
                 |
                 v
           AgentOrchestrator
            |            |
         Retriever     Tools
```

Keep secrets in env. This repo ships stubs so you can learn the shape without a cloud bill.
