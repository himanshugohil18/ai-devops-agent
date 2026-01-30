from agent.log_collector import collect_logs
from agent.analyzer import analyze_logs

print("\n🚀 REAL AI DEVOPS AGENT STARTED\n")

logs = collect_logs()

if not logs:
    print("❌ No logs found")
    exit()

result = analyze_logs(logs)

print("🧠 ANALYSIS RESULT\n")
for item in result["details"]:
    print(item)
