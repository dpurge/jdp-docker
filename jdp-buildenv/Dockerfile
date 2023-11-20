FROM ubuntu:22.04

ARG GOLANG_VERSION=1.20.4
ARG TASKFILE_VERSION=3.30.1
ARG YQ_VERSION=4.35.2

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN apt update; apt install -y --no-install-recommends \
    ca-certificates \
    calibre \
    curl \
    git \
    golang \
    gpg \
    jq \
	libopengl0 \
	libxcb-cursor0 \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-venv \
    python3-wheel \
    tzdata \
    unzip \
	xz-utils \
    zsh \
    ; apt clean
    
RUN mkdir /workspace

RUN cd /usr/local/bin \
    && curl -sSL https://github.com/go-task/task/releases/download/v${TASKFILE_VERSION}/task_linux_amd64.tar.gz -o task_linux_amd64.tar.gz \
    && tar -xzvf task_linux_amd64.tar.gz task \
    && rm task_linux_amd64.tar.gz

RUN cd /usr/local/bin \
    && curl -sSL https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_amd64.tar.gz -o yq_linux_amd64.tar.gz \
    && tar --transform='s/_linux_amd64//' -xzvf yq_linux_amd64.tar.gz ./yq_linux_amd64 \
    && rm yq_linux_amd64.tar.gz

COPY python-requirements.txt /workspace/python-requirements.txt

RUN pip install --no-cache-dir -r /workspace/python-requirements.txt \
    && rm /workspace/python-requirements.txt

ENV DEBIAN_FRONTEND=dialog

WORKDIR /workspace
VOLUME ["/workspace"]
