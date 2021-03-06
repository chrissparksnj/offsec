#/usr/bin/bash
git clone https://github.com/laramies/theHarvester.git
cd theHarvester
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install python3.7
sudo apt install python3-pip
pip3 install -r requirements/base.txt
pip3 install aiohttp

echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc 
echo "HARVESTER INSTALLED. RUN python3 theHarvester.py -h"
