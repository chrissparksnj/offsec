#!/bin/bash

if [ $# -eq 0 ]; then 
	PORT="22";
else 
	PORT=$1;
fi 

msfconsole -x "use auxiliary/scanner/ssh/ssh_enumusers;
set user_file $HOME/gitclones/opsec/fastlists/unix_users.txt;
set RHOSTS $ip;
set RPORT $PORT; 
run;
"

