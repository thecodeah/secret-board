FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app/web
ARG SB_SECRET_KEY=xxx
RUN python manage.py collectstatic