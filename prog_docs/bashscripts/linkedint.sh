#!/bin/bash


git clone https://github.com/vysecurity/LinkedInt.git
cd LinkedInt
sed -i '/pkg-resources==0.0.0/d' ./requirements.txt
pip install -r requirements.txt
python2 LinkedInt.py



