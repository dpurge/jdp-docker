ARG UBUNTU_VERSION=26.04
FROM --platform=linux/amd64 ubuntu:${UBUNTU_VERSION}

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ARG YQ_VERSION=4.49.2

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN apt update && apt upgrade --yes && apt install --yes --no-install-recommends \
    ca-certificates \
    curl \
    dirmngr \
    gpg \
    gpg-agent \
    jq \
    neovim \
    net-tools \
    sudo \
    unzip \
    xmlstarlet \
    xz-utils \
    tzdata \
    && apt clean \
    && gpg -k \
    && mkdir -p /usr/local/bin \
    && cd /usr/local/bin \
    && curl -Lo /tmp/yq_linux_amd64.tar.gz https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_amd64.tar.gz \
    && tar --transform='s/_linux_amd64//' -xzvf /tmp/yq_linux_amd64.tar.gz ./yq_linux_amd64 \
    && rm -f /tmp/*.tar.gz /tmp/*.zip /tmp/*.deb

ENV DEBIAN_FRONTEND=dialog
