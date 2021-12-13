
FROM acaratti/pypoet:3.8

RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install

COPY . .
