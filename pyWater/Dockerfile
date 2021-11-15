# Dockerfile

# Pull base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# # Install dependencies
# RUN pip install pipenv
# COPY Pipfile Pipfile.lock /code/
# RUN pipenv install --system

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# Copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

