FROM debian:buster
RUN apt update -y
RUN su -l _apt -s /bin/bash
USER _apt
WORKDIR /tmp/
