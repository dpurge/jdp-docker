FROM jdp-ubuntu:latest

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ARG CUELANG_VERSION=0.15.1
ARG DENO_VERSION=2.3.5
ARG GORELEASER_VERSION=2.9.0
ARG GRADLE_VERSION=9.2.1
ARG GOTASK_VERSION=3.43.3
ARG JSONNET_VERSION=0.21.0
ARG KUBECTL_VERSION=1.34.2
ARG RUST_VERSION=1.83.0
ARG TIMONI_VERSION=0.25.2
ARG TOFU_VERSION=1.10.7

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

ENV PATH="$PATH:/opt/gradle/gradle-9.2.1/bin"

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN mkdir -p /home/developer /workspace \
    && groupadd -r developer \
    && useradd -r -g developer -s /bin/bash -d /home/developer developer \
    && usermod -a -G sudo developer \
    && chown -R developer:developer /home/developer \
    && chown -R developer:developer /workspace \
    && curl -fsSL https://dl.k6.io/key.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/k6-archive-keyring.gpg > /dev/null \
    && echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list \
    && apt update \
    && apt install --yes --no-install-recommends \
    build-essential \
    default-jre \
    git \
    golang \
    k6 \
    pip \
    python3 \
    && apt clean \
    && cd /usr/local/bin \
    && curl -Lo /tmp/task_linux_amd64.tar.gz https://github.com/go-task/task/releases/download/v${GOTASK_VERSION}/task_linux_amd64.tar.gz \
    && tar -xzvf /tmp/task_linux_amd64.tar.gz task \
    && curl -Lo /tmp/goreleaser_Linux_x86_64.tar.gz https://github.com/goreleaser/goreleaser/releases/download/v${GORELEASER_VERSION}/goreleaser_Linux_x86_64.tar.gz \
    && tar -xzvf /tmp/goreleaser_Linux_x86_64.tar.gz goreleaser \
    && curl -Lo /tmp/rust-x86_64-unknown-linux-gnu.tar.gz https://static.rust-lang.org/dist/rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz \
    && mkdir /tmp/rust \
    && tar xvzf /tmp/rust-x86_64-unknown-linux-gnu.tar.gz -C /tmp/rust --strip-components=1 --exclude=rust-docs \
    && /tmp/rust/install.sh --without=rust-docs \
    && rm -rf /tmp/rust \
    && curl -Lo /tmp/deno-x86_64-unknown-linux-gnu.zip https://github.com/denoland/deno/releases/download/v${DENO_VERSION}/deno-x86_64-unknown-linux-gnu.zip \
    && unzip /tmp/deno-x86_64-unknown-linux-gnu.zip \
    && curl -Lo /tmp/jsonnet-go_linux_amd64.deb https://github.com/google/go-jsonnet/releases/download/v${JSONNET_VERSION}/jsonnet-go_${JSONNET_VERSION}_linux_amd64.deb \
    && dpkg -i /tmp/jsonnet-go_linux_amd64.deb \
    && curl -Lo /tmp/cue_linux_amd64.tar.gz https://github.com/cue-lang/cue/releases/download/v${CUELANG_VERSION}/cue_v${CUELANG_VERSION}_linux_amd64.tar.gz \
    && tar -xzvf /tmp/cue_linux_amd64.tar.gz cue \
    && curl -Lo /tmp/timoni_linux_amd64.tar.gz https://github.com/stefanprodan/timoni/releases/download/v${TIMONI_VERSION}/timoni_${TIMONI_VERSION}_linux_amd64.tar.gz \
    && tar -xzvf /tmp/timoni_linux_amd64.tar.gz timoni \
    && curl -Lo /tmp/tofu_linux_amd64.tar.gz https://github.com/opentofu/opentofu/releases/download/v${TOFU_VERSION}/tofu_${TOFU_VERSION}_linux_amd64.tar.gz \
    && tar -xzvf /tmp/tofu_linux_amd64.tar.gz tofu \
    && curl -Lo /tmp/gradle-bin.zip https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip -d /opt/gradle /tmp/gradle-bin.zip \
    && rm -f /tmp/*.tar.gz /tmp/*.zip /tmp/*.deb \
    && curl -LO "https://dl.k8s.io/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl" \
    && chmod +x kubectl

ENV DEBIAN_FRONTEND=dialog

USER developer
WORKDIR /workspace
