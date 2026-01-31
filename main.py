from agent.analyzer import analyze_logs
from agent.log_loader import load_logs
from agent.output_formatter import format_analysis


def main():
    print("🚀 REAL AI DEVOPS AGENT STARTED")

    # Load logs from mounted volume
    logs = load_logs("/logs")

    if not logs:
        print("❌ No valid logs found")
        return

    print("\n🧠 Sending logs to LOCAL AI...\n")

    # Run AI analysis
    result = analyze_logs(logs)

    print("🧠 ANALYSIS RESULT")

    # ✅ Proper structured output (NO raw print)
    format_analysis(result)


if __name__ == "__main__":
    main()
