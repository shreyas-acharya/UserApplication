FROM python:3.10-slim

RUN mkdir /src
RUN mkdir /src/App

COPY /App /src/App
COPY pyproject.toml /src

WORKDIR /src
RUN pip3 install poetry
RUN poetry --version
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry", "run", "uvicorn", "App.main:app", "--reload"]
