
if [ $# -eq 0 ]; then
  echo "Please pass in a ip"
else
  nmap -sV -Pn -vv --script=mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122 $1 -p 3306
fi