def rule_based_analysis(log: str):
    rules = [
        {
            "match": "OOMKilled",
            "issue": "Container ran out of memory",
            "root_cause": "Memory limit too low or memory leak",
            "solution": "Increase memory limits or optimize application",
            "command": "kubectl edit deployment <deployment-name>"
        },
        {
            "match": "CrashLoopBackOff",
            "issue": "Pod restarting continuously",
            "root_cause": "App crash or bad health check",
            "solution": "Check container logs and probes",
            "command": "kubectl logs <pod-name>"
        },
        {
            "match": "ECONNREFUSED",
            "issue": "Service connection refused",
            "root_cause": "Service down or wrong port",
            "solution": "Check service and container port",
            "command": "docker ps && docker logs <container>"
        },
        {
            "match": "npm ERR!",
            "issue": "Node dependency failure",
            "root_cause": "Dependency conflict",
            "solution": "Fix package.json or use legacy deps",
            "command": "npm install --legacy-peer-deps"
        }
    ]

    for rule in rules:
        if rule["match"] in log:
            return rule

    return {
        "issue": "Unknown issue",
        "root_cause": "Not matched by rules",
        "solution": "Manual inspection required",
        "command": "Check logs manually"
    }
