#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Please specify a ip address by exporting: eg: ./smb_version_ms.sh <ipaddress>";
else
  sudo msfconsole -x " use auxiliary/scanner/smb/smb_version; set RHOSTS $1; run; exit"
fi
