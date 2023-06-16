FROM python:3.9-slim-buster

# Install build tools and dependencies
RUN apt-get update \
    && apt-get install -y build-essential default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]