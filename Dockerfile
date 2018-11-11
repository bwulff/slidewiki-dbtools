FROM ubuntu:16.04

ENV PYTHONUNBUFFERED 1

# gettext provides envsubst (used in entrypoint.sh)
RUN apt-get update && apt-get install -y python python-pip

RUN mkdir /app
ADD add_suspend_users.py /app
RUN pip install pymongo

