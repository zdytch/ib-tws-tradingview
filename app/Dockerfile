FROM python:3.11-slim-bullseye as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc

WORKDIR /usr/src

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .


########## Production

FROM base as prod

RUN pipenv install --system --deploy --ignore-pipfile

COPY ./src .

# CMD your command here


########## Base Dev

FROM base as base-dev

RUN pipenv install --system --deploy --ignore-pipfile --dev


########## Development

FROM base-dev as dev

# CMD your command here
