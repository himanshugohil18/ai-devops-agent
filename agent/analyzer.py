from agent.ai_engine import ai_analysis


def detect_issues_from_logs(logs: str):
    issues = []

    if "error" in logs.lower():
        issues.append({
            "severity": "HIGH",
            "root_cause": "Application error detected in logs",
            "fix": "Inspect stack trace and fix application error",
            "verify": "Re-run application and confirm error is resolved",
        })

    if "docker" in logs.lower() and "failed" in logs.lower():
        issues.append({
            "severity": "HIGH",
            "root_cause": "Docker operation failed",
            "fix": "Check Dockerfile and rebuild image",
            "verify": "docker build && docker run",
        })

    if "kubernetes" in logs.lower():
        issues.append({
            "severity": "MEDIUM",
            "root_cause": "Kubernetes-related configuration issue",
            "fix": "Validate Kubernetes YAML manifests",
            "verify": "kubectl apply --dry-run=client",
        })

    return issues


def analyze_logs(logs: str):
    detected_issues = detect_issues_from_logs(logs)

    ai_response = ai_analysis(logs)

    severity = "LOW"
    if detected_issues:
        severity = detected_issues[0]["severity"]

    verdict_message = (
        "Immediate attention required"
        if severity == "HIGH"
        else "System appears stable but monitoring is advised"
    )

    return {
        "summary": {
            "type": ai_response.get("analysis_type", "LOG_ANALYSIS"),
            "severity": severity,
        },
        "issues": detected_issues,
        "verdict": {
            "message": verdict_message,
            "auto_fix": False,
        },
    }
