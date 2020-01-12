FROM python:3.6.8
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["gunicorn", "--workers=4", "--bind=0.0.0.0:5002", "application:app"]
COPY . .
RUN pytest --cov
