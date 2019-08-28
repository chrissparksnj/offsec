if [ $# -eq 0 ]; then
  echo "Please pass in a ip"
else

msfconsole -x "use auxiliary/scanner/mssql/mssql_ping; set RHOSTS $1; run; exit"
fi