# Calculator Web App

A small web application for performing basic calculations and storing results in a database. The app is containerized with Docker.

## Setup Instructions

### Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/zlKxrsan/calculator.git
   cd calculator

   ```

1. `pip install -r requirements.txt`
1. `python -m app.main`

### Docker

1. Docker Build: `docker build -t calculator-app .`
1. Docker Run: `docker run -p 5000:5000 calculator-app`
1. Open in localhost:5000

## Features

- basic calculations (+, -, \*, /)
- Stores results in a history
- portability through Docker
