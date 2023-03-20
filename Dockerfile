FROM python:3.11-slim as builder
WORKDIR src
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry export --format=requirements.txt --without-hashes --no-cache -o requirements.txt && \
    pip install -r requirements.txt --target=/src/packages

# FROM cgr.dev/chainguard/python:latest
FROM python:3.11-slim
WORKDIR src
COPY /App .
COPY --from=builder /src/packages /src
RUN apt-get remove --auto-remove -y --allow-remove-essential e2fsprogs ncurses-base ncurses-bin libdb5.3 libncursesw6 libtinfo6 libcom-err2 libgcrypt20
ENTRYPOINT ["python", "main.py"]
