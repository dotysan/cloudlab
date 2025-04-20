#! /usr/bin/env bash
# needs to be run as root/sudo
set -xe

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get --yes purge \
    emacs-common \
    iso-codes \
    libgtk-3-common \
    locales \
    python3-babel \
    python3-botocore \
    snapd \
    ubuntu-pro-client \
    #
apt-get --yes install \
    mc \
    #
apt-get --yes autopurge
apt-get --yes upgrade
apt-get --yes upgrade
