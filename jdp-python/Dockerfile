FROM python:3.13.3-slim

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN apt update && apt upgrade --yes && apt install --yes --no-install-recommends \
    expat \
    gcc \
    minizip \
    ; apt clean \
    ; mkdir -p /home/application /app \
    ; groupadd -r application \
    ; useradd -r -g application -s /sbin/nologin -d /home/application application \
    ; chown -R application:application /home/application /app \
    ; chmod -R 550 /app

USER application

COPY src/requirements.txt /requirements-python.txt
RUN pip install --no-cache-dir -r /requirements-python.txt
