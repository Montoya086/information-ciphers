FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

COPY server.py .

CMD ["python", "server.py"] 