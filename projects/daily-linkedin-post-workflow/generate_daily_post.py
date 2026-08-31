import argparse
import json
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent


def load_topics():
    with (ROOT / "content_calendar.json").open(encoding="utf-8") as f:
        return json.load(f)


def load_font(size: int, bold: bool = False):
    names = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    lines = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_centered_lines(draw, lines, box, font, fill, spacing=8):
    left, top, right, bottom = box
    heights = [draw.textbbox((0, 0), line, font=font)[3] for line in lines]
    total = sum(heights) + spacing * max(0, len(lines) - 1)
    y = top + (bottom - top - total) / 2
    for line, height in zip(lines, heights):
        width = draw.textbbox((0, 0), line, font=font)[2]
        draw.text((left + (right - left - width) / 2, y), line, font=font, fill=fill)
        y += height + spacing


def build_graphic(run_date: date, topic, output_path: Path):
    width = height = 1200
    background = "#101820"
    ink = "#F5F7FA"
    muted = "#AEBBC7"
    teal = "#29C3B1"
    gold = "#F4B942"
    panel = "#1A2833"
    line = "#496170"
    image = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(image)

    for x in range(0, width, 60):
        draw.line((x, 0, x, height), fill="#15232D", width=1)
    for y in range(0, height, 60):
        draw.line((0, y, width, y), fill="#15232D", width=1)

    label_font = load_font(24, bold=True)
    title_font = load_font(58, bold=True)
    hook_font = load_font(30)
    step_font = load_font(25, bold=True)
    small_font = load_font(22)

    draw.rounded_rectangle((70, 62, 343, 112), radius=8, fill=teal)
    draw.text((91, 75), "DATA ENGINEERING", font=label_font, fill=background)
    draw.text((70, 141), topic["theme"].upper(), font=title_font, fill=ink)

    hook_lines = wrap_text(draw, topic["hook"], hook_font, 1050)
    y = 225
    for line_text in hook_lines[:3]:
        draw.text((72, y), line_text, font=hook_font, fill=muted)
        y += 43

    draw.text((72, 372), topic["diagram_title"].upper(), font=label_font, fill=gold)
    draw.line((72, 410, 1128, 410), fill=line, width=2)

    steps = topic["visual_steps"]
    gap = 24
    box_width = (1056 - gap * (len(steps) - 1)) / len(steps)
    box_top, box_bottom = 485, 690
    centers = []
    for index, step in enumerate(steps):
        left = 72 + index * (box_width + gap)
        right = left + box_width
        centers.append(((left + right) / 2, (box_top + box_bottom) / 2))
        draw.rounded_rectangle((left, box_top, right, box_bottom), radius=12, fill=panel, outline=teal if index in (0, len(steps) - 1) else line, width=3)
        draw.ellipse((left + 16, box_top + 16, left + 54, box_top + 54), fill=gold if index == len(steps) - 1 else teal)
        number = str(index + 1)
        number_width = draw.textbbox((0, 0), number, font=small_font)[2]
        draw.text((left + 35 - number_width / 2, box_top + 21), number, font=small_font, fill=background)
        lines = wrap_text(draw, step, step_font, box_width - 32)
        draw_centered_lines(draw, lines, (left + 14, box_top + 55, right - 14, box_bottom - 12), step_font, ink)

    for index in range(len(centers) - 1):
        x1 = 72 + (index + 1) * box_width + index * gap
        x2 = x1 + gap
        y_mid = (box_top + box_bottom) / 2
        draw.line((x1 + 3, y_mid, x2 - 6, y_mid), fill=gold, width=5)
        draw.polygon([(x2 - 6, y_mid - 9), (x2 + 3, y_mid), (x2 - 6, y_mid + 9)], fill=gold)

    draw.rounded_rectangle((72, 776, 1128, 1010), radius=14, fill="#F5F7FA")
    draw.text((106, 811), "PRACTICAL TAKEAWAY", font=label_font, fill="#176C63")
    takeaway_lines = wrap_text(draw, topic["takeaway"], load_font(34, bold=True), 970)
    take_y = 865
    for line_text in takeaway_lines[:3]:
        draw.text((106, take_y), line_text, font=load_font(34, bold=True), fill="#17232C")
        take_y += 47

    draw.line((72, 1075, 1128, 1075), fill=line, width=2)
    draw.text((72, 1101), f"OCHOLI IDAKWO  |  SENIOR DATA ENGINEER  |  {run_date.isoformat()}", font=small_font, fill=muted)
    draw.text((951, 1101), "Kasala95", font=small_font, fill=teal)
    image.save(output_path, format="PNG", optimize=True)


def build_post(run_date: date) -> str:
    topics = load_topics()
    topic = topics[run_date.toordinal() % len(topics)]
    diagram = topic["diagram"].replace("\\n", "\n")
    post = f"""# LinkedIn Post Draft - {run_date.isoformat()}

Theme: {topic["theme"]}

## Post Copy

{topic["hook"]}

{topic["body"]}

{topic["takeaway"]}

I documented the architecture and implementation patterns in my public data engineering portfolio: https://kasala95.github.io/data-engineering-portfolio/

{topic["discussion_prompt"]}

Suggested hashtags: #DataEngineering #AnalyticsEngineering #DataGovernance #CloudData #DataArchitecture

## Diagram Documentation

{topic["diagram_title"]}

LinkedIn-ready graphic: `generated/{run_date.isoformat()}-linkedin-graphic.png`

```mermaid
{diagram}
```

## Publishing Checklist

- Review the post for tone and accuracy.
- Add one personal sentence based on recent work, learning, or interview preparation.
- Upload the generated 1200 x 1200 PNG graphic with the post.
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
    graphic_path = generated / f"{run_date.isoformat()}-linkedin-graphic.png"
    latest_graphic_path = generated / "latest-linkedin-graphic.png"
    dated_path.write_text(content, encoding="utf-8")
    latest_path.write_text(content, encoding="utf-8")
    topics = load_topics()
    topic = topics[run_date.toordinal() % len(topics)]
    build_graphic(run_date, topic, graphic_path)
    build_graphic(run_date, topic, latest_graphic_path)
    print(f"Wrote {dated_path}")
    print(f"Wrote {latest_path}")
    print(f"Wrote {graphic_path}")
    print(f"Wrote {latest_graphic_path}")


if __name__ == "__main__":
    main()
