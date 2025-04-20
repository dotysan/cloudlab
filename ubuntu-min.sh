#! /usr/bin/env bash
# needs to be run as root/sudo
set -xe

# TODO: detect if this has already run and skip it
#  - howabout see if apt-get update has never been run?
exit

export DEBIAN_FRONTEND=noninteractive
apt-get update
systemctl stop unattended-upgrades.service
apt-get --yes purge \
    emacs-common \
    iso-codes \
    libgtk-3-common \
    polkitd \
    python3-babel \
    python3-botocore \
    snapd \
    ubuntu-pro-client \
    unattended-upgrades \
    #
apt-get --yes install \
    atop \
    btop \
    mc \
    #
apt-get --yes autopurge
apt-get --yes dist-upgrade
apt-get install --reinstall linux-firmware

linux_ver=$(dpkg-query -W -f='${Version}\n' linux-generic)
linux_ver="${linux_ver%.*}"
linux_rel=$(uname --kernel-release)
linux_rel="${linux_rel%-*}"
if [[ "$linux_ver" != "$linux_re" ]]
then shutdown -r now
exit
