FROM debian:bullseye
RUN apt update -y
RUN apt install wget make gcc subversion openssl autoconf automake libtool libssl-dev build-essential -y
WORKDIR /tmp/
RUN svn co https://svn.nmap.org/nmap --non-interactive --trust-server-cert
WORKDIR /tmp/nmap
RUN ./configure
RUN make
WORKDIR /tmp/nmap/ncat
RUN ./configure
RUN make
RUN cat ncat | base64 > ncat.b64
