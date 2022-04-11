FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev shadow

COPY requirements.txt /app
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

RUN useradd app_user
RUN chown -R app_user:app_user /app

USER app_user:app_user




