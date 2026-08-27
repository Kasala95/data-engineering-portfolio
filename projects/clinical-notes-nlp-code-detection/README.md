# Clinical Notes NLP Code Detection

> Portfolio recreation using synthetic data. Inspired by real senior data engineering patterns, but it contains no employer code, schemas, credentials, or confidential data.

## What This Demonstrates
A synthetic NLP pipeline that scans fake clinical notes for diagnosis terms and flags candidate codes missing from billed-code records.

## Compliance Note
Uses fully synthetic notes and candidate codes. Outputs are designed for human review, not automatic billing changes.

## LinkedIn Summary
Built an NLP pipeline for de-identified clinical notes to support targeted, auditable billing-code review.

## Run
`python3 detect_candidate_codes.py` writes candidate review findings.
