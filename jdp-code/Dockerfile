FROM jdp-build:latest

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ARG CODE_VERSION=4.106.2

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

USER root
ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN curl -Lo /tmp/code-server_amd64.deb https://github.com/coder/code-server/releases/download/v${CODE_VERSION}/code-server_${CODE_VERSION}_amd64.deb \
    && dpkg -i /tmp/code-server_amd64.deb \
    && rm -f /tmp/*.tar.gz /tmp/*.zip /tmp/*.deb

ENV DEBIAN_FRONTEND=dialog
USER developer

EXPOSE 8080
CMD ["code-server", "--disable-telemetry", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]