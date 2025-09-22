#!/bin/bash

set -e

sudo apt update
sudo apt install -y musl-dev
sudo ln -sf /usr/lib/x86_64-linux-musl/libc.so /lib/libc.musl-x86_64.so.1
conda install -c conda-forge libstdcxx-ng -y
pip install -r requirements.txt
