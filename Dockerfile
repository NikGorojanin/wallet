FROM python:3.12.5-slim

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # poetry:
  POETRY_VERSION=1.8.2 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update \
  && apt-get install -y \
    bash \
    default-libmysqlclient-dev build-essential pkg-config \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION" && poetry --version \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry install
COPY . .
EXPOSE 8000

CMD poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000
#CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
