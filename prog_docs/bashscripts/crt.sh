#!/bin/bash

domain=$1
curl -s https://crt.sh/?q=%.$domain| grep TD | grep -v style | cut -d  '>' -f2 | cut -d '<' -f1 | sort | uniq | grep -v Identity




