# ===============================
# Base Image
# ===============================
FROM python:3.11-slim

# ===============================
# Environment
# ===============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===============================
# Working directory
# ===============================
WORKDIR /app

# ===============================
# System dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Python dependencies
# ===============================
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ===============================
# Application code
# ===============================
COPY agent ./agent
COPY main.py .

# ===============================
# Logs directory
# ===============================
RUN mkdir -p /logs

# ===============================
# Run app
# ===============================
CMD ["python", "main.py"]
