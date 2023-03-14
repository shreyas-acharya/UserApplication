FROM python:3.11-slim as builder
WORKDIR src
COPY pyproject.toml poetry.lock .
RUN pip install poetry && \
    poetry export --format=requirements.txt --without-hashes --no-cache -o requirements.txt && \
    pip install -r requirements.txt --target=/src/packages

# FROM cgr.dev/chainguard/python:latest
FROM python:3.11-slim
WORKDIR src
COPY /App .
COPY --from=builder /src/packages /src
ENTRYPOINT ["python", "main.py"]
