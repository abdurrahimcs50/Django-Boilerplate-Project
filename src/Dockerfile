# syntax=docker/dockerfile:1

# This Dockerfile sets up a Python environment for your application.
# For more information on Dockerfiles, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

# Set the base Python version for the Docker image.
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-alpine3.18 as base

# The PYTHONDONTWRITEBYTECODE environment variable prevents Python from writing .pyc files.
# This is useful in a container environment to keep the image size small.
ENV PYTHONDONTWRITEBYTECODE=1

# The PYTHONUNBUFFERED environment variable prevents Python from buffering stdout and stderr.
# This is useful in a container environment to ensure that logs are emitted immediately,
# which can help with debugging if the application crashes.
ENV PYTHONUNBUFFERED=1

# Set the working directory for the Docker image.
# This is the directory that commands will run in by default.
WORKDIR /usr/src/app

# Upgrade pip to the latest version.
# This ensures that you have the latest features and security fixes.
RUN pip install --upgrade pip

# Copy the requirements.txt file into the Docker image.
# This file lists the Python packages that your application depends on.
COPY ./requirements.txt .

# Install the Python packages listed in requirements.txt.
# These packages will be available in the Python environment inside the Docker container.
RUN pip install -r requirements.txt

# Copy the rest of your application's source code into the Docker image.
# This includes all of your application's code and resources.
COPY . .


# # Expose the port that the application listens on.
# EXPOSE 8000

# # Run the application.
# CMD gunicorn 'Django_Boilerplate_Project.wsgi' --bind=0.0.0.0:8000
