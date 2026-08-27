# Scheduled LinkedIn Content Workflow Diagram

```mermaid
flowchart TD
  A[Daily GitHub Actions Schedule] --> B[Checkout Repository]
  B --> C[Run generate_daily_post.py]
  C --> D[Select Topic From Calendar]
  D --> E[Create LinkedIn Draft]
  E --> F[Embed Mermaid Diagram]
  F --> G[Write Date-Stamped Markdown]
  G --> H[Update latest-linkedin-post.md]
  H --> I[Commit Draft To Repository]
  I --> J[Manual Review]
  J --> K[Publish On LinkedIn]
```

## Review Gate

The workflow intentionally stops at draft generation. Automated publishing to LinkedIn should only be added after the account has an approved LinkedIn API integration, proper user authorization, and a final human review step.
