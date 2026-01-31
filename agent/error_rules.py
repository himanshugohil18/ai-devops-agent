def rule_based_analysis(logs):
    issues = []

    for filename, content in logs.items():
        text = content.lower()

        if "out of memory" in text or "oomkilled" in text:
            issues.append({
                "file": filename,
                "issue": "Out of Memory",
                "cause": "Memory limit too low",
                "fix": "Increase container/JVM memory"
            })

        if "permission denied" in text:
            issues.append({
                "file": filename,
                "issue": "Permission Denied",
                "cause": "Wrong file permissions",
                "fix": "Check chmod / ownership"
            })

        if "connection refused" in text:
            issues.append({
                "file": filename,
                "issue": "Service Down",
                "cause": "Port/service not reachable",
                "fix": "Check service & port mapping"
            })

        if "finished: failure" in text or "build failed" in text:
            issues.append({
                "file": filename,
                "issue": "Jenkins Build Failed",
                "cause": "Pipeline/script error",
                "fix": "Check Jenkinsfile logs"
            })

    return issues