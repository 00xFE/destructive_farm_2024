FROM python:3.13.3-slim-bookworm

# FROM debian:bookworm-slim
# RUN apt-get update && \
#	DEBIAN_FRONTEND=noninteractive apt-get install -qq \
#	git \
#    python3 \
#    python3-pip \
#    sqlite3

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    sqlite3 \
    vim

COPY . .
WORKDIR /server

RUN pip3 install -r ./requirements.txt
CMD ["sh", "./start_server.sh"]
