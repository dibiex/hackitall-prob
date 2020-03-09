FROM ubuntu:18.04
RUN \
    apt update && apt upgrade && \
    apt install python3.7 -y && \
    apt install python3-pip -y  && \
    pip3 install flask && \
    pip3 install pymongo
RUN mkdir /code
WORKDIR /code
ADD . /code/
