#!/bin/bash
#######################################################################
#             Build python for specific docker images                 #
# You will need to copy them out of the container and on to your host #
#      docker cp <CONTAINER ID>:/tmp/tmp_localpython.tar.gz .         #
#######################################################################

function check_for_docker(){
    docker_group=0
    for i in $(groups); do
        if [[ $i == 'docker' ]]; then
            echo '[*] User in Docker group'
	    docker_group=1
	fi
    done
    if [[ $docker_group == 0 ]]; then
        echo '[*] Docker group not found, exiting.'
	exit
    fi
}

function build_alpine_3_17_1() {
    /usr/bin/docker build -t python-builder-alpine-3-17-1 -f containers/alpine/3_17_1/Dockerfile .
}

function build_debian_bullseye() {
    /usr/bin/docker build -t python-builder-debian-bullseye -f containers/debian/bullseye/Dockerfile .
}

function build_debian_bullseye_client() {
    /usr/bin/docker build -t python-builder-debian-bullseye-client -f containers/debian/bullseye/client.dockerfile .
}

function build_debian_buster() {
    /usr/bin/docker build -t python-builder-debian-buster -f containers/debian/buster/Dockerfile .
}

function build_debian_buster_client() {
    /usr/bin/docker build -t python-builder-debian-buster-client -f containers/debian/buster/client.dockerfile .
}


############################
# Functions to run on exec #
############################

check_for_docker
build_alpine_3_17_1 &
build_debian_bullseye &
build_debian_bullseye_client &
build_debian_buster &
build_debian_buster_client &
