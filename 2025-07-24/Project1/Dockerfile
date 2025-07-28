FROM python:3.11-slim-bookworm

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends gcc build-essential && pip install --upgrade pip && pip install -r requirements.txt && apt-get remove -y gcc build-essential && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]