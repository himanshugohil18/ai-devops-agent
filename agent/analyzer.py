from agent.error_rules import rule_based_analysis
from agent.ai_engine import ai_analysis

def analyze_logs(logs):
    rule_result = rule_based_analysis(logs)

    if rule_result:
        return {
            "analysis_type": "RULE_BASED",
            "details": rule_result
        }

    ai_result = ai_analysis(logs)
    return {
        "analysis_type": "AI_BASED",
        "details": ai_result
    }
