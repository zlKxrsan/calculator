FROM python:3.12.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Flask port
EXPOSE 5000

ENTRYPOINT ["python", "-m", "app.main"]
