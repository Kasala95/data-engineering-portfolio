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

## Case Study Detail

This project demonstrates a compliance-aware NLP review workflow using fully synthetic clinical notes. The script detects diagnosis terms, maps them to candidate codes, compares them with billed-code records, and writes a review queue for missing candidates.

The design intentionally stops at human review. In healthcare and revenue-cycle workflows, candidate detection should support analysts and coding teams rather than automatically changing billing records.

Production equivalent patterns:

- secure document ingestion and de-identification
- medical terminology extraction with rule-based and model-assisted detection
- precision-focused review queues for uncertain findings
- audit trails for reviewer decisions
- monitoring for terminology drift and model performance changes

Reviewer signal:

This project shows I understand how to build NLP-supported workflows in regulated environments without over-automating sensitive decisions.
