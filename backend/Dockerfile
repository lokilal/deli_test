FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt --no-cache-dir

CMD python3 /app/manage.py migrate && \
    python3 /app/manage.py collectstatic --no-input&& \
    gunicorn backend.wsgi:application --bind 0.0.0.0:8000

