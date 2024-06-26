#!/bin/bash

docker build -t monerominer -f cryptominers/monero/Dockerfile .
docker build -t deroheminer -f cryptominers/dero/Dockerfile .
docker build -t fileserver -f fileserver.dockerfile .
