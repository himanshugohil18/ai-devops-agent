# 🚀 AI DevOps Incident Analysis System (AIOps)

An AI-powered DevOps system that automatically analyzes real application and Docker logs using a local LLM engine to generate structured incident reports.

This project demonstrates how modern DevOps and SRE teams can integrate AI into operational workflows for faster, smarter, and more reliable incident response.

---

## 🏗️ Architecture

```
+----------------------+
|   Real Log Files     |
| (app, docker, etc.)  |
+----------+-----------+
           |
           v
+----------------------+
|  Docker Container    |
|  ai-devops-agent     |
|----------------------|
| Python Log Loader    |
| Validation Layer     |
| Rule-Based Checks    |
+----------+-----------+
           |
           v
+----------------------+
|   Local LLM Engine   |
|      (Ollama)        |
+----------+-----------+
           |
           v
+-------------------------------+
| AI Incident Analysis Output   |
|-------------------------------|
| Incident Type                |
| Severity                     |
| Root Cause                   |
| Fix / Remediation            |
| Verification Steps           |
+-------------------------------+
```

---

## ✨ Features

- Log ingestion using Docker volume mounts  
- Aggregation of multiple log sources  
- AI-based incident classification  
- Root cause analysis using LLM  
- Actionable remediation suggestions  
- Fully offline (no cloud APIs)  
- Secure enterprise-ready design  
- Extensible toward Kubernetes & auto-fix systems  

---

## 🛠 Tech Stack

- Python  
- Docker  
- Ollama (Local LLM runtime)  
- Linux  
- AIOps principles  

---

## ⚙️ How It Works

1. Logs are mounted into the container from the host system  
2. Python service reads and validates all logs  
3. Combined logs are sent to local LLM via Ollama  
4. AI generates structured incident report  
5. Output is printed in terminal  

---

## ▶️ Run Locally

### Build Image
```bash
docker build -t ai-devops-agent .
```

### Run Container
```bash
docker run -it \
  -v "C:\Users\Himanshu\Downloads\ai-devops-agent\real-logs:/logs" \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  ai-devops-agent
```

---

## 📊 Sample Output

```
AI DEVOPS INCIDENT ANALYSIS

Incident Type : DOCKER_AUTO_FIX
Severity      : HIGH

Issue #1:
Root Cause : Application error detected in logs
Fix        : Inspect stack trace and fix application error
Verify     : Re-run application and confirm error is resolved

Issue #2:
Root Cause : Docker operation failed
Fix        : Check Dockerfile and rebuild image
Verify     : docker build && docker run
```

---

## 🔮 Future Enhancements

- Kubernetes YAML validation  
- Auto-remediation scripts  
- Slack / Email alerts  
- Log streaming  
- Web dashboard UI  
- Integration with CI/CD pipelines  

---

## 👨‍💻 Author

Himanshu Gohil  
DevOps Engineer | AIOps | Python | Docker | LLM  

---

## 🎯 Why This Project Matters

This project simulates how real-world DevOps teams can:

- Reduce MTTR (Mean Time to Resolution)  
- Automate incident response  
- Apply AI in production operations  
- Build cloud-independent AIOps platforms  

---

## 📜 License

MIT License
