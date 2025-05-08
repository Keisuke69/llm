FROM mcr.microsoft.com/devcontainers/python:3.10

# 追加のパッケージをインストール
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    build-essential \
    git \
    curl \
    wget \
    vim

# Python関連ツールのインストール
RUN pip install --upgrade pip \
    && pip install pylint autopep8 black flake8 mypy

# 作業ディレクトリの設定
WORKDIR /workspace

# ユーザー権限の設定
RUN chown -R vscode:vscode /workspace
USER vscode
