# Data Quality And Observability Framework

> Portfolio recreation using synthetic data. Inspired by real senior data engineering patterns, but it contains no employer code, schemas, credentials, or confidential data.

## What This Demonstrates
A lightweight quality framework that tests uniqueness, nulls, accepted ranges, freshness, and pipeline readiness using synthetic event data.

## Checks
Includes uniqueness, null thresholds, range checks, freshness checks, and machine-readable JSON reporting.

## LinkedIn Summary
Built automated data quality and observability checks to catch silent pipeline issues before publication.

## Run
`python3 validate_events.py` runs checks and writes a quality report.

## Case Study Detail

This project demonstrates a practical quality gate for analytics data. The input intentionally contains a duplicate record and a missing business key so the validation report has meaningful failures. In real data systems, those issues should be detected before dashboards, ML jobs, or executive metrics consume the dataset.

The validation script produces structured JSON that can be connected to alerts, deployment gates, or incident triage workflows. The point is not that every check passes; the point is that the system identifies failures clearly.

Production equivalent patterns:

- Great Expectations or dbt tests for table-level and column-level checks
- freshness monitoring for ingestion pipelines
- uniqueness and not-null controls on business keys
- alert routing to Slack, PagerDuty, Datadog, or CloudWatch
- runbooks that distinguish source-data issues from transformation failures

Reviewer signal:

This project shows I treat trust, monitoring, and failure visibility as part of the product, not an afterthought.
