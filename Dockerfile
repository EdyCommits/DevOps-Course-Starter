# Base
FROM python as base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /code

ENV PATH "/code:/root:/root/.poetry/bin:${PATH}"

# add and install python requirements
COPY pyproject.toml poetry.lock /code/
RUN poetry install

# Copy the rest of the code
COPY / /code/

# Development 
FROM base as development
EXPOSE 5100
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0", "-p", "5100"]

# Production
FROM base as production
EXPOSE 5000
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "todo_app.app:create_app()", "--access-logfile", "gunicorn-access.log", "--log-file", "gunicorn.log"]

