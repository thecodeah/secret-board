FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

# Set a temporary secret key as it's required to run any manage.py command.
ARG SB_SECRET_KEY=xxx
RUN python manage.py collectstatic
