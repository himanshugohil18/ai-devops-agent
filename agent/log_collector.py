import os

LOG_DIR = "/logs"   # Docker-mounted directory

def collect_logs():
    collected = {}

    if not os.path.exists(LOG_DIR):
        print("❌ Log directory not found:", LOG_DIR)
        return collected

    for file in os.listdir(LOG_DIR):
        file_path = os.path.join(LOG_DIR, file)

        if os.path.isfile(file_path):
            with open(file_path, "r", errors="ignore") as f:
                collected[file] = f.read()

    return collected
