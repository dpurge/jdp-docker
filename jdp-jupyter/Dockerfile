FROM ubuntu:kinetic

MAINTAINER dpurge

ENV DEBIAN_FRONTEND=noninteractive

# Install system
RUN apt-get update; \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        netbase \
        wget \
        tzdata \
		\
		build-essential \
		cmake \
		gcc \
		g++ \
		\
		libjpeg-dev \
		libpng-dev \
		libpq-dev \
		libssl-dev \
		libzmq3-dev \
		libopencv-dev \
		\
		git \
		unzip \
		imagemagick \
		gnuplot \
		gnuplot-x11 \
		graphviz \
		\
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        python3-wheel \
        python3-setuptools \
        python3-opencv \
    ; \
    rm -rf /var/lib/apt/lists/*

# Cleanup
RUN apt-get autoremove -y && \
    apt-get clean autoclean && \
    rm -rf /var/lib/apt/lists/*

# Python packages
RUN pip3 install --upgrade pip && \
    pip3 install setuptools --upgrade && \
    pip3 install \
		wheel \
		tensorflow \
		ipykernel \
		docutils \
		jupyter \
		pyyaml \
		pylint \
		h5py \
		numpy \
		pandas \
		sklearn \
		scipy \
		matplotlib \
		seaborn \
		pydotplus \
		keras \
		opencv-python \
		imutils \
		sqlalchemy \
		pyautogui

ENV DEBIAN_FRONTEND=dialog
ENV PATH=/root/.local/bin:$PATH

COPY .jupyter /root/.jupyter

EXPOSE 8888

WORKDIR /workspace
VOLUME ["/workspace"]
