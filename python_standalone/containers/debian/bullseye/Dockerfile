FROM debian:bullseye
RUN apt update -y
RUN apt install wget make gcc zlib1g-dev -y
RUN apt install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.6 libgdm-dev libdb4o-cil-dev libpcap-dev -y
#RUN useradd -ms /bin/bash _apt # should already exist
RUN su -l _apt -s /bin/bash
USER _apt
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
