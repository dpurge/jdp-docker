FROM jdp-ubuntu

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN apt install --yes --no-install-recommends \
    build-essential \
    curl \
    git \
    golang \
    gpg \
    jq \
    pip \
    python3 \
    sudo \
    unzip \
    xmlstarlet \
    ; gpg -k \
    ; gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69 \
    ; echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | tee /etc/apt/sources.list.d/k6.list \
    ; apt update \
    ; apt install k6 \
    ; apt clean \
    ; cd /usr/local/bin \
    ; curl -Lo /tmp/task_linux_amd64.tar.gz https://github.com/go-task/task/releases/download/v3.43.3/task_linux_amd64.tar.gz \
    ; tar -xzvf /tmp/task_linux_amd64.tar.gz task \
    ; curl -Lo /tmp/yq_linux_amd64.tar.gz https://github.com/mikefarah/yq/releases/download/v4.45.4/yq_linux_amd64.tar.gz \
    ; tar --transform='s/_linux_amd64//' -xzvf /tmp/yq_linux_amd64.tar.gz ./yq_linux_amd64 \
    ; curl -Lo /tmp/deno-x86_64-unknown-linux-gnu.zip https://github.com/denoland/deno/releases/download/v2.3.5/deno-x86_64-unknown-linux-gnu.zip \
    ; unzip /tmp/deno-x86_64-unknown-linux-gnu.zip \
    ; curl -Lo /tmp/jsonnet-go_linux_amd64.deb https://github.com/google/go-jsonnet/releases/download/v0.21.0/jsonnet-go_0.21.0_linux_amd64.deb \
    ; dpkg -i /tmp/jsonnet-go_linux_amd64.deb \
    ; rm -f /tmp/*.tar.gz /tmp/*.zip /tmp/*.deb \
    ; curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh -s -- -y \
    ; curl --proto '=https' --tlsv1.3 -sSf https://get.opentofu.org/install-opentofu.sh | sh -s -- --install-method deb \
    ; curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    ; chmod +x kubectl \
    ; mkdir -p /home/developer /workspace \
    ; groupadd -r developer \
    ; useradd -r -g developer -s /bin/bash -d /home/developer developer \
    ; usermod -a -G sudo developer \
    ; chown -R developer:developer /home/developer /workspace \
    ; echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV DEBIAN_FRONTEND=dialog

USER developer
WORKDIR /workspace
VOLUME ["/workspace"]
