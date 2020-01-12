FROM python:3.6.8
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["gunicorn", "--workers=4", "--bind=0.0.0.0:8001", "application:app"]
COPY . .
ARG MYSQL_USER=${MYSQL_USER}
ARG MYSQL_PASSWORD=${MYSQL_PASSWORD}
ARG MYSQL_IP=${MYSQL_IP}
ARG MYSQL_DB=${MYSQL_DB}
ARG MYSQL_DB_TEST=${MYSQL_DB_TEST}
ARG MYSQL_KEY=${MYSQL_KEY}
RUN pytest --cov

