FROM quay.io/centos/centos:stream8
RUN dnf update -y
RUN dnf groupinstall "Development Tools" -y
RUN dnf install wget openssl-devel subversion -y
WORKDIR /tmp/
RUN svn co https://svn.nmap.org/nmap --non-interactive --trust-server-cert
WORKDIR /tmp/nmap
RUN ./configure
RUN make
WORKDIR /tmp/nmap/ncat
RUN ./configure
RUN make
RUN cat ncat | base64 > ncat.b64
