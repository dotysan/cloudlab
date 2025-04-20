ubuntu_min = """#!/bin/bash
#! /usr/bin/env bash
set -x
echo 'start' >>/hello.log
#euo pipefail

export DEBIAN_FRONTEND=noninteractive
apt-get update |tee -a /hello.log
echo 'apt-get --yes purge' >>/hello.log
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
apt-get --yes autopurge |tee -a /hello.log
apt-get --yes upgrade |tee -a /hello.log
"""
