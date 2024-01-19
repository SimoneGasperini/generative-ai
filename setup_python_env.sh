#! /usr/bin/env bash

wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
tar xzf Python-3.10.0.tgz
rm Python-3.10.0.tgz
cd Python-3.10.0/
sudo apt-get install curl gcc libbz2-dev libev-dev libffi-dev libgdbm-dev liblzma-dev libncurses-dev libreadline-dev libsqlite3-dev libssl-dev make tk-dev wget zlib1g-dev
./configure --enable-optimizations
sudo make altinstall
cd ..
python3.10 -m venv venvs/llm
source venvs/llm/bin/activate
pip3 install transformers
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install replicate llama_index
pip3 install pillow pypdf
