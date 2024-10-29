FROM debian:bookworm-slim AS builder

ENV CARGO_HOME="/opt/.cargo"

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

WORKDIR /opt

RUN apt-get update && \
  apt-get install -y --no-install-recommends ca-certificates curl

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm

ENV CARGO_HOME="/opt/.cargo"
ENV PATH="$CARGO_HOME/bin/:$PATH"
ENV PYTHONUNBUFFERED=True
ENV UV_LINK_MODE=copy

WORKDIR /opt

COPY --from=builder --chown=vscode: $CARGO_HOME $CARGO_HOME
