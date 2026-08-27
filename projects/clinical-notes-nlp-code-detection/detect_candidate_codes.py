import csv
from pathlib import Path

root = Path(__file__).resolve().parent
terms = {"diabetes": "E11", "heart failure": "I50", "kidney disease": "N18", "pneumonia": "J18", "hypertension": "I10"}
findings = []
with (root / "data" / "synthetic_clinical_notes.csv").open() as f:
    for row in csv.DictReader(f):
        text = row["clinical_note"].lower()
        detected = {code for term, code in terms.items() if term in text}
        billed = set(row["billed_codes"].split("|")) if row["billed_codes"] else set()
        missing = sorted(detected - billed)
        if missing:
            findings.append({"note_id": row["note_id"], "missing_candidate_codes": "|".join(missing), "review_status": "needs_human_review"})
(root / "outputs").mkdir(exist_ok=True)
with (root / "outputs" / "candidate_code_findings.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["note_id", "missing_candidate_codes", "review_status"])
    writer.writeheader()
    writer.writerows(findings)
print(f"Wrote {len(findings)} candidate findings")
