FROM alpine:3.17.1
RUN apk update
RUN apk add --no-cache ca-certificates wget make gcc libc-dev libpcap-dev zlib-dev zlib-static libressl-dev
WORKDIR /tmp/
RUN wget -c http://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
RUN tar -zxvf Python-3.9.2.tgz
WORKDIR /tmp/Python-3.9.2
RUN mkdir /tmp/.localpython
RUN ./configure --prefix=/tmp/.localpython
RUN make
RUN make install
RUN /tmp/.localpython/bin/python3.9 -m pip install --upgrade pip
RUN /tmp/.localpython/bin/pip3 install requests
WORKDIR /tmp/
RUN tar -zcvf tmp_localpython.tar.gz /tmp/.localpython
