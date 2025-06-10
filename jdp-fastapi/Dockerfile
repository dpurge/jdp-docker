FROM registry.home.arpa:5000/jdp-python:latest

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

EXPOSE 8080

COPY src/requirements.txt /requirements-fastapi.txt
RUN pip install --no-cache-dir -r /requirements-fastapi.txt

CMD [ "fastapi", "run", "/app/main.py", "--proxy-headers", "--port", "8080"]
