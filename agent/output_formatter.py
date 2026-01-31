def format_analysis(result: dict):
    print("\n" + "=" * 55)
    print("🤖 AI DEVOPS INCIDENT ANALYSIS")
    print("=" * 55)

    summary = result.get("summary", {})
    issues = result.get("issues", [])
    verdict = result.get("verdict", {})

    # 🔹 Incident Summary
    print("\n📌 INCIDENT SUMMARY")
    print("-" * 40)
    print(f"Incident Type : {summary.get('type', 'UNKNOWN')}")
    print(f"Severity      : {summary.get('severity', 'UNKNOWN')}")

    # 🔹 Issues Found
    print("\n🚨 ISSUES FOUND")
    print("-" * 40)

    if not issues:
        print("✅ No critical issues detected")
    else:
        for idx, issue in enumerate(issues, start=1):
            print(f"\n🔹 Issue #{idx}")
            print(f"Severity   : {issue.get('severity', 'UNKNOWN')}")
            print(f"Root Cause : {issue.get('root_cause', 'N/A')}")
            print(f"Fix        : {issue.get('fix', 'N/A')}")
            print(f"Verify     : {issue.get('verify', 'N/A')}")

    # 🔹 Final Verdict
    print("\n📊 FINAL VERDICT")
    print("-" * 40)
    print(verdict.get("message", "No verdict provided"))
    print(f"Auto-Fix Applied : {verdict.get('auto_fix', False)}")

    print("\n" + "=" * 55)
