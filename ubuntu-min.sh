#! /usr/bin/env bash
# needs to be run as root/sudo
set -xe

# TODO: detect if this has already run and skip it

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get --yes purge \
    emacs-common \
    iso-codes \
    libgtk-3-common \
    python3-babel \
    python3-botocore \
    snapd \
    ubuntu-pro-client \
    unattended-upgrades \
    #
apt-get --yes install \
    mc \
    #
apt-get --yes autopurge
apt-get --yes dist-upgrade
apt-get install --reinstall linux-firmware

# since we added new kernel
#shutdown -r now
# doh! this script runs on each boot
