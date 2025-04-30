FROM python:3.12.2-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./templates ./templates
COPY ./static ./static

ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Flask port
EXPOSE 5000

ENTRYPOINT ["python", "app/main.py"]
