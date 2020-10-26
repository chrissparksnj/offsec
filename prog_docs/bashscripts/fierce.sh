#!/bin/bash

git clone https://github.com/mschwager/fierce.git
cd fierce
pip3 install -r requirements.txt
python3 ./fierce/fierce.py -h
