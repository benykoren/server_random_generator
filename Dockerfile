FROM python:3.8

WORKDIR /app
COPY src/ /app/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "/app/src/server/random_server.py"]
