def rule_based_analysis(logs: str):
    rules = [
        {
            "match": "OOMKilled",
            "issue": "Out of Memory",
            "root_cause": "Memory limit too low",
            "solution": "Increase container memory",
            "command": "kubectl edit deployment <deployment>"
        },
        {
            "match": "CrashLoopBackOff",
            "issue": "Pod crash loop",
            "root_cause": "App crash or bad probe",
            "solution": "Check logs and probes",
            "command": "kubectl logs <pod>"
        },
        {
            "match": "npm ERR!",
            "issue": "Node dependency error",
            "root_cause": "Dependency conflict",
            "solution": "Fix package.json",
            "command": "npm install --legacy-peer-deps"
        },
        {
            "match": "ECONNREFUSED",
            "issue": "Connection refused",
            "root_cause": "Service not reachable",
            "solution": "Check service/port",
            "command": "docker ps && docker logs <container>"
        }
    ]

    for rule in rules:
        if rule["match"] in logs:
            return rule

    return None
