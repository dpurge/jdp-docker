FROM ubuntu:22.04

#ARG GOLANG_VERSION=1.20.4
ARG TASKFILE_VERSION=3.34.1
ARG YQ_VERSION=4.41.1

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN apt update; apt install -y --no-install-recommends \
    ca-certificates \
    calibre \
    curl \
    fonts-arphic-ukai \
    fonts-arphic-uming \
    fonts-hosny-amiri \
    fonts-noto \
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
    yt-dlp \
    zsh \
    ; apt clean

RUN cd /usr/local/bin &&\
    mkdir -p /etc/apt/keyrings &&\
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg &&\
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_21.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list &&\
    apt update &&\
    apt install  -y --no-install-recommends nodejs &&\
    apt clean &&\
    curl -sSL https://github.com/go-task/task/releases/download/v${TASKFILE_VERSION}/task_linux_amd64.tar.gz -o task_linux_amd64.tar.gz &&\
    tar -xzvf task_linux_amd64.tar.gz task &&\
    rm task_linux_amd64.tar.gz &&\
    curl -sSL https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_amd64.tar.gz -o yq_linux_amd64.tar.gz &&\
    tar --transform='s/_linux_amd64//' -xzvf yq_linux_amd64.tar.gz ./yq_linux_amd64 &&\
    rm yq_linux_amd64.tar.gz &&\
    mkdir /workspace

COPY python-requirements.txt /workspace/python-requirements.txt

RUN pip install --no-cache-dir -r /workspace/python-requirements.txt &&\
    rm /workspace/python-requirements.txt

ENV DEBIAN_FRONTEND=dialog

WORKDIR /workspace
VOLUME ["/workspace"]
