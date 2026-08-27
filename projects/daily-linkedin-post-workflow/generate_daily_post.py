import argparse
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_topics():
    with (ROOT / "content_calendar.json").open(encoding="utf-8") as f:
        return json.load(f)


def build_post(run_date: date) -> str:
    topics = load_topics()
    topic = topics[run_date.toordinal() % len(topics)]
    diagram = topic["diagram"].replace("\\n", "\n")
    post = f"""# LinkedIn Post Draft - {run_date.isoformat()}

Theme: {topic["theme"]}

## Post Copy

{topic["hook"]}

{topic["body"]}

Practical takeaway: {topic["takeaway"]}

Portfolio context: This post can link back to the data engineering portfolio at https://kasala95.github.io/data-engineering-portfolio/

Suggested hashtags: #DataEngineering #AnalyticsEngineering #CloudData #DataGovernance #Snowflake #Databricks

## Diagram Documentation

{topic["diagram_title"]}

```mermaid
{diagram}
```

## Publishing Checklist

- Review the post for tone and accuracy.
- Add one personal sentence based on recent work, learning, or interview preparation.
- Upload the Mermaid diagram as an image or paste the diagram text into a documentation carousel.
- Publish manually on LinkedIn.
- Save the final LinkedIn URL back into this repository if desired.
"""
    return post


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Date to generate, formatted YYYY-MM-DD")
    args = parser.parse_args()
    run_date = date.fromisoformat(args.date) if args.date else date.today()
    generated = ROOT / "generated"
    generated.mkdir(exist_ok=True)
    content = build_post(run_date)
    dated_path = generated / f"{run_date.isoformat()}-linkedin-post.md"
    latest_path = generated / "latest-linkedin-post.md"
    dated_path.write_text(content, encoding="utf-8")
    latest_path.write_text(content, encoding="utf-8")
    print(f"Wrote {dated_path}")
    print(f"Wrote {latest_path}")


if __name__ == "__main__":
    main()
