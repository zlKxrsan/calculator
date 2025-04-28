# Taschenrechner Web-App

Eine kleine Web-App zum Rechnen und Speichern von Ergebnissen in einer Azure SQL Datenbank.

## Setup

1. `pip install -r requirements.txt`
2. `python app/main.py`
3. Docker Build: `docker build -t calculator-app .`
4. Docker Run: `docker run -p 5000:5000 calculator-app`

## Features

- Grundrechenarten (+, -, \*, /)
- Speicherung der Rechenhistorie
- Docker und Azure Deployment ready
