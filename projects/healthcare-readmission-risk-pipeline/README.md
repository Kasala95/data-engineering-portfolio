# Healthcare Readmission Risk Pipeline

> Portfolio recreation using synthetic data. Inspired by real senior data engineering patterns, but it contains no employer code, schemas, credentials, or confidential data.

## What This Demonstrates
A synthetic healthcare ML-style pipeline that engineers readmission risk features and generates daily patient-level risk scores without using protected health information.

## Modeling Pattern
Uses an interpretable logistic scoring formula to demonstrate feature engineering, calibration thinking, and risk banding.

## LinkedIn Summary
Developed a healthcare machine learning pipeline to predict 30-day readmission risk for proactive discharge planning.

## Run
`python3 score_readmission_risk.py` generates synthetic risk scores.

## Case Study Detail

This project recreates the data engineering shape of a healthcare risk scoring pipeline without using real patient data. It uses synthetic clinical-style fields such as age, prior admissions, abnormal lab count, medication count, specialty, and social risk flag.

The scoring approach is deliberately interpretable so reviewers can see how risk factors influence output bands. In production, a project like this would require stronger model validation, clinical governance, privacy review, drift monitoring, and responsible use controls.

Production equivalent patterns:

- HIPAA-aware ingestion and de-identification processes
- feature pipelines for labs, diagnoses, medications, vitals, and admissions
- model registry and batch scoring with MLflow or equivalent tooling
- monitoring for data drift, missing feeds, and score distribution changes
- human-reviewed clinical workflow integration

Reviewer signal:

This project shows I can connect data engineering, ML infrastructure, and regulated-domain thinking.
