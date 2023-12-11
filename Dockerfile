FROM python:3.9


RUN apt-get update && \
    apt-get install -y rabbitmq-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


COPY start_services.sh /


RUN chmod +x /start_services.sh


CMD ["/start_services.sh"]

