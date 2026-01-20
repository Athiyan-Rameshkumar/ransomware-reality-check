# Data Handling & Privacy Model

## Core Principle
All data provided to the Ransomware Reality Check tool is processed ephemerally.

## Data Lifecycle
1. User uploads a file
2. File is validated (type + size)
3. File is processed in-memory or in a temporary directory
4. File is deleted immediately after analysis
5. No data is retained, logged, or shared

## What We Do NOT Do
- No credentials collected
- No live system access
- No monitoring
- No data resale
- No training on user data

## Logs
Application logs contain:
- Timestamps
- File size
- Processing success/failure

Application logs do NOT contain:
- User data
- Identifiers
- File contents

## Compliance Alignment
This model aligns with:
- Data minimization principles
- Privacy-by-design practices
- NGO trust expectations

