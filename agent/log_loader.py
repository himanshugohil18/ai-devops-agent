import os

def load_logs(path="/logs"):
    print(f"\n📂 LOG LOADER DEBUG")
    print(f"📍 Path checked: {path}")

    if not os.path.exists(path):
        print("❌ /logs directory does NOT exist")
        return ""

    files = os.listdir(path)
    print(f"📄 Files found: {files}")

    if not files:
        print("❌ No files inside /logs")
        return ""

    combined_logs = ""

    for file in files:
        file_path = os.path.join(path, file)
        print(f"➡ Reading file: {file_path}")

        if file.endswith(".log"):
            with open(file_path, "r", errors="ignore") as f:
                content = f.read()
                print(f"📏 {file} size: {len(content)} chars")
                combined_logs += f"\n===== {file} =====\n{content}\n"

    if not combined_logs.strip():
        print("❌ Log content is EMPTY after reading")
    else:
        print("✅ Logs successfully loaded")

    return combined_logs
