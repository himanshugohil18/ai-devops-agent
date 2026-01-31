import os
from langchain_ollama import OllamaLLM


def ai_analysis(logs: str) -> dict:
    """
    AI-powered log analysis using LOCAL Ollama model.
    Focus: Docker & container issues
    """

    # Ollama connection (from Docker env)
    OLLAMA_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://host.docker.internal:11434"
    )

    # ⚠️ Use SMALL model (phi / mistral / tinyllama)
    llm = OllamaLLM(
        model="phi",          # <-- IMPORTANT: low RAM, fast
        base_url=OLLAMA_URL,
        temperature=0.1
    )

    # 
    prompt = f"""
You are a Senior DevOps SRE AI Agent.

Rules:
- Analyze ALL issues in the logs
- Focus ONLY on Docker & container runtime
- Detect multiple incidents if present
- Assign SEVERITY (LOW / MEDIUM / HIGH / CRITICAL)
- Provide EXACT shell commands
- No generic advice, no explanations

Logs:
{logs}

Output strictly in this format:

ISSUE #:
SEVERITY:
ROOT CAUSE:
FIX COMMAND:
VERIFY:
"""

    try:
        response = llm.invoke(prompt)

        return {
            "analysis_type": "DOCKER_AUTO_FIX",
            "details": response.strip()
        }

    except Exception as e:
        return {
            "analysis_type": "AI_ERROR",
            "details": str(e)
        }
