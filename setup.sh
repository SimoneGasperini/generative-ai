#! /usr/bin/env bash
 
# Stop script if any command fails
set -e

# Install required dependencies
sudo apt-get install curl gcc libbz2-dev libev-dev libffi-dev libgdbm-dev liblzma-dev libncurses-dev libreadline-dev libsqlite3-dev libssl-dev make tk-dev wget zlib1g-dev -y

wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
tar xzf Python-3.10.0.tgz
rm Python-3.10.0.tgz
cd Python-3.10.0/
 
# Configure and install Python
./configure --enable-optimizations
sudo make altinstall
cd ..
 
# Create virtual environment
python3.10 -m venv venvs/llm
 
# Activate virtual environment
source venvs/llm/bin/activate
 
# Check if virtual environment is activated
if [ "$VIRTUAL_ENV" != "" ]; then
    echo "Virtual environment activated. Installing packages..."
    # Install packages using pip
    pip3 install transformers pypdf pillow
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip3 install replicate llama_index
else
    echo "Error: Virtual environment not activated. Please activate the virtual environment before running this script."
fi
