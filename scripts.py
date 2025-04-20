ubuntu_min = """
#! /usr/bin/env bash
set -xeuo pipefail

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
apt-get --yes autopurge
apt-get --yes upgrade
"""
