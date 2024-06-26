FROM debian:latest
RUN apt update -y && apt upgrade -y && apt dist-upgrade -y
RUN apt install golang git zip -y
WORKDIR "/root/build/"
RUN git clone https://github.com/deroproject/derohe.git
WORKDIR "/root/build/derohe/"
RUN bash build_all.sh
#RUN ls /root/build/derohe/build/dero_linux_amd64/

RUN cat /root/build/derohe/build/dero_linux_amd64/dero-miner-linux-amd64 | base64 > /root/build/dero.b64
WORKDIR "/root/build/"
RUN rm -rf /root/build/derohe
COPY fileserver/fileserver/tearmeup.py .
RUN chmod 755 tearmeup.py

RUN apt install python3 -y

RUN ./tearmeup.py dero.b64
RUN rm dero.b64 && rm tearmeup.py
