import pandas as pd

def analyze_identity(csv_path):
    df = pd.read_csv(csv_path)
    findings = []

    # MFA Disabled
    mfa_disabled = df[df["AuthenticationRequirement"] != "multiFactorAuthentication"]
    if not mfa_disabled.empty:
        findings.append({
            "signal_id": "MFA_DISABLED",
            "severity": "high",
            "affected_entities": mfa_disabled["UserPrincipalName"].unique().tolist(),
            "explanation": "Some accounts can be accessed using only a password."
        })

    # Risky Sign-ins
    risky = df[df["RiskLevelAggregated"].isin(["high", "medium"])]
    if not risky.empty:
        findings.append({
            "signal_id": "RISKY_SIGN_INS",
            "severity": "medium",
            "affected_entities": risky["UserPrincipalName"].unique().tolist(),
            "explanation": "Risky sign-in behavior was detected."
        })

    # Legacy Authentication
    legacy = df[df["ClientAppUsed"].isin(["IMAP", "POP", "SMTP"])]
    if not legacy.empty:
        findings.append({
            "signal_id": "LEGACY_AUTH_ENABLED",
            "severity": "high",
            "affected_entities": legacy["UserPrincipalName"].unique().tolist(),
            "explanation": "Legacy authentication protocols were detected."
        })

    return findings

