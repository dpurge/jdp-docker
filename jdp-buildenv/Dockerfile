FROM ubuntu:22.04

#ARG GOLANG_VERSION=1.20.4
ARG TASKFILE_VERSION=3.34.1
ARG YQ_VERSION=4.41.1

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN apt update; apt install -y --no-install-recommends \
    ca-certificates \
    calibre \
    curl \
    ffmpeg \
    fonts-arphic-ukai \
    fonts-arphic-uming \
    fonts-hosny-amiri \
    fonts-noto \
    git \
    golang \
    gpg \
    hugo \
    jq \
    libopengl0 \
    libxcb-cursor0 \
    nodejs \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-venv \
    python3-wheel \
    tzdata \
    unzip \
    xz-utils \
    yt-dlp \
    zsh \
    ; apt clean

COPY python-requirements.txt /tmp/python-requirements.txt
COPY install.sh /tmp/install.sh

RUN pip install --no-cache-dir -r /tmp/python-requirements.txt && rm /tmp/python-requirements.txt
RUN sh /tmp/install.sh && rm /tmp/install.sh

ENV DEBIAN_FRONTEND=dialog

WORKDIR /workspace
VOLUME ["/workspace"]
