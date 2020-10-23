#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit

else
	git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/
        cd setoolkit
	pip3 install -r requirements.txt
	python setup.py
fi
