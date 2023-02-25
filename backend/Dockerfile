FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
RUN apt update
RUN apt install -y --assume-yes python3-dev libpq-dev build-essential python3-pip


COPY requirements requirements

COPY requirements/base.txt requirements/base.txt

RUN pip3 install -r requirements/base.txt
RUN pip3 install -r requirements/tests.txt
