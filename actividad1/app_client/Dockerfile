FROM ubuntu:latest

RUN apt-get update \
    && apt-get -y install iputils-ping \
    && apt-get -y install iproute2 \
    && apt-get -y install dnsutils \
    && apt-get -y install python3 \
    && apt-get -y install python3-pip \
    && apt-get -y install vim \
    && apt-get -y install sqlite

ADD client.py /app_client/

WORKDIR /app_client/
