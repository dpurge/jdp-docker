FROM ubuntu:24.04

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN apt update && apt upgrade --yes && apt install --yes --no-install-recommends \
    ca-certificates \
    tzdata \
    ; apt clean \
    ; mkdir -p /usr/local/bin

ENV DEBIAN_FRONTEND=dialog