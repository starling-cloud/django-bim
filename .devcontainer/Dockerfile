# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Ensure Poetry is in the PATH
ENV PATH="/root/.local/bin:${PATH}"

# Copy the project's dependencies file to the container
COPY pyproject.toml poetry.lock* /app/

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application
COPY . /app
