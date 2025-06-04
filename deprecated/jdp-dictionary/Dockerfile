FROM ubuntu:22.04

RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker

RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update \
  && apt-get install -y \
    dict \
    dictd \
    dictfmt \
    dictzip \
    tini \
  && rm -rf /var/lib/apt/lists/*

# RUN useradd -ms /bin/bash dictd
# USER dictd

EXPOSE 2628

CMD ["tini", "dictd", "-dnodetach"]
