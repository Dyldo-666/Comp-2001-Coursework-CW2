FROM python:3.11-slim

# System deps + GPG + unixODBC
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates gnupg unixodbc unixodbc-dev \
  && rm -rf /var/lib/apt/lists/*

# Add Microsoft package repository (NO apt-key, keep single [ ... ] block)
RUN mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /etc/apt/keyrings/microsoft.gpg \
  && chmod 644 /etc/apt/keyrings/microsoft.gpg \
  && curl -fsSL https://packages.microsoft.com/config/debian/12/prod.list \
     | sed 's|/usr/share/keyrings/microsoft-prod.gpg|/etc/apt/keyrings/microsoft.gpg|g' \
     > /etc/apt/sources.list.d/microsoft-prod.list \
  && apt-get update \
  && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

