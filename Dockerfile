FROM python:3.12.2-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app ./app
COPY ./templates ./templates
COPY ./static ./static

CMD ["python", "app/main.py"]
