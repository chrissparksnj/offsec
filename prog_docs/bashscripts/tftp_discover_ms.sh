

#!/bin/bash

echo "This program takes a while to run";

msfconsole -x "use scanner/tftp/tftpbrute; set RHOSTS $ip; set THREADS 10; run; exit"
