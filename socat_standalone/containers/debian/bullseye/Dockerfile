FROM debian:bullseye
RUN apt update -y
RUN apt install wget make gcc openssl git -y
#RUN useradd -ms /bin/bash _apt # should already exist
RUN su -l _apt -s /bin/bash
USER _apt
WORKDIR /tmp/
RUN mkdir git
RUN cd git/
RUN git clone https://github.com/3ndG4me/socat.git
WORKDIR /tmp/socat/
RUN ./configure
RUN make
RUN cat socat | base64 > socat.b64
