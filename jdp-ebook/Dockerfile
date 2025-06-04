FROM jdp-build

ARG VERSION=${VERSION}
ARG BRANCH=${BRANCH}
ARG COMMIT=${COMMIT}

ENV APP_VERSION=${VERSION}
ENV GIT_BRANCH=${BRANCH}
ENV GIT_COMMIT=${COMMIT}

ENV DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC

RUN sudo apt install --yes --no-install-recommends \
    anki \
    calibre \
    ffmpeg \
    fonts-arphic-ukai \
    fonts-arphic-uming \
    fonts-hosny-amiri \
    fonts-noto \
    ; sudo apt clean

ENV DEBIAN_FRONTEND=dialog