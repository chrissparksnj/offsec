#!/bin/bash

git clone https://github.com/fwaeytens/dnsenum.git
sudo apt-get install libnet-ip-perl -y
sudo apt-get install libnet-dns-perl -y
sudo apt-get install libnet-netmask-perl -y
sudo apt-get install libxml-writer-perl -y 
sudo apt-get install libstring-random-perl -y
cd dnsenum
perl dnsenum.pl
