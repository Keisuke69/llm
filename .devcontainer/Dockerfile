FROM mcr.microsoft.com/devcontainers/python:3.10

# 追加のパッケージをインストール
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    build-essential \
    git \
    curl \
    wget \
    vim

# 作業ディレクトリの設定
WORKDIR /workspace

# ユーザー権限の設定
RUN chown -R vscode:vscode /workspace
USER vscode

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/vscode/.local/bin:${PATH}"

WORKDIR /home/vscode
RUN uv venv
