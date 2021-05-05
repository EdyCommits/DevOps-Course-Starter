FROM python as base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /code

ENV PATH "/code:/root:/root/.poetry/bin:${PATH}"