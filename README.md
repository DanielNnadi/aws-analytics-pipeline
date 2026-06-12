# AWS Cloud-Native Analytics Pipeline

End-to-end ETL pipeline on AWS.

## Architecture

Data Source → API Gateway → Lambda → S3 → Lambda → PostgreSQL RDS → Power BI

## Results

- 10,000+ daily records processed
- Sub-5-minute source-to-dashboard latency
- Infrastructure as Code (CloudFormation)

## Files

- `cloudformation/` — AWS infrastructure templates
- `lambda/` — Python ETL functions

