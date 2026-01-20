# Entra ID Sign-in Log Schema (v1)

## Required Columns
- UserPrincipalName
- AuthenticationRequirement
- AuthenticationDetails
- RiskLevelAggregated
- ClientAppUsed
- CreatedDateTime

## Optional Columns
- IPAddress
- Location
- ConditionalAccessStatus

## Notes
- MFA is considered disabled if AuthenticationRequirement != 'multiFactorAuthentication'
- Legacy auth is inferred from ClientAppUsed

