FROM debian:latest
RUN apt update -y && apt upgrade -y && apt dist-upgrade -y
RUN apt install golang git zip python3 -y
WORKDIR "/root/build/"
RUN git clone https://github.com/deroproject/derohe.git
WORKDIR "/root/build/derohe/"
RUN bash build_all.sh
RUN cat /root/build/derohe/build/dero_linux_amd64/dero-miner-linux-amd64 | base64 > /root/build/dero.b64
WORKDIR "/root/build/"
RUN rm -rf /root/build/derohe
COPY fileserver/tearmeup.py .
RUN chmod 755 tearmeup.py
RUN ./tearmeup.py dero.b64
RUN rm dero.b64 && rm tearmeup.py
