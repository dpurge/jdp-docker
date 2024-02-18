#!/bin/bash

mkdir -p /usr/local/bin
cd /usr/local/bin

curl -sSL https://github.com/go-task/task/releases/download/v3.34.1/task_linux_amd64.tar.gz -o task_linux_amd64.tar.gz
tar -xzvf task_linux_amd64.tar.gz task
rm task_linux_amd64.tar.gz

curl -sSL https://github.com/mikefarah/yq/releases/download/v4.41.1/yq_linux_amd64.tar.gz -o yq_linux_amd64.tar.gz
tar --transform='s/_linux_amd64//' -xzvf yq_linux_amd64.tar.gz ./yq_linux_amd64
rm yq_linux_amd64.tar.gz

mkdir /workspace
