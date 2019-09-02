## Pentesting Notes and Commands

### Install Instructions
`git clone https://github.com/chrissparksnj/offsec.git`

`cd offsec/`

`source venv/bin/activate`

`pip install -r requirements.txt`



### Running Program
```
$ python opsec_auto.py -h

usage: opsec_auto.py [-h] [-pk] [-wa] [-sq] [-nm] [-dn] [-sb] [-en] [-sh]
                     [-ft] [-sl] [-sm] [-nf] [-a] [-gm] [-ul] [-it] [-fl]
                     [--crt-search] [--flush-db] [--subdomains] [--raw-ip]
                     [--domain DOMAIN] [--version]

Automatically spin up everything from the guide.offsecnewbie.com walk through

optional arguments:
  -h, --help           show this help message and exit
  -pk, --packages      show interesting packages and their install instructions
  -wa, --web-app       show web-app commands
  -sq, --sql           show web-app commands
  -nm, --nmap          show nmap commands
  -dn, --dns           shows all dns commands
  -sb, --smb           shows all smb commands
  -en, --enum          shows all smb commands
  -sh, --ssh           shows all ssh commands
  -ft, --ftp           shows all ftp commands
  -sl, --ssl           shows all ssl commands
  -sm, --smtp          shows all smtp commands
  -nf, --nfs           show all nfs commands
  -a, --all            shows all smtp commands
  -gm, --get-modules   shows methodology offered within the tutorial
  -ul, --useful-links  shows useful link
  -fl, --fast-lists    get lists that are useful, fast!
  --version            show program's version number and exit
```


# Example Usage
### Get interesting packages

```
python opsec_auto.py -pk
+Git Packages---+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| program name  | program link                                                                   | program_instructions                                                                 |
+---------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| the_harvester | https://github.com/laramies/theHarvester.git                                   | python3 -m pip install -r requirements.txt                                           |
| recon-ng      | https://github.com/lanmaster53/recon-ng.git                                    | pip install -r REQUIREMENTS                                                          |
| wfuzz         | https://github.com/xmendez/wfuzz.git                                           | python setup.py install                                                              |
| shocker       | https://github.com/nccgroup/shocker.git                                        | python shocker.py                                                                    |
| seclist       | https://github.com/danielmiessler/SecLists.git                                 | nothing                                                                              |
| wfuzz         | https://github.com/xmendez/wfuzz.git                                           | sudo apt-get install wfuzz libcurl4-openssl-dev libssl-dev; pip install pycurl       |
| searchsploit  | https://github.com/offensive-security/exploitdb.git                            | wget https://bit.ly/30xEoiM | bash                                                   |
| metaploit     | https://github.com/rapid7/metasploit-framework.git                             | wget https://bit.ly/32114rF | bash                                                   |
| whatweb       | https://github.com/urbanadventurer/WhatWeb.git                                 | https://github.com/urbanadventurer/WhatWeb/wiki/Installation                         |
| dnsrecon      | https://github.com/darkoperator/dnsrecon.git                                   | pip install -r requirements.txt                                                      |
| dnsmap.txt    | https://raw.githubusercontent.com/kkirsche/wordlistgenerator/master/dnsmap.txt | wget                                                                                 |
| smbmap        | https://github.com/ShawnDEvans/smbmap.git                                      | pip install -r requirements                                                          |
| nmblookup     | nmblookup                                                                      | apt install samba-common-bin                                                         |
| medusa        | medusa                                                                         | apt-get install medusa                                                               |
| nbtscan       | nbtscan                                                                        | sudo apt-get install nbtscan                                                         |
| nikto         | nikto                                                                          | sudo apt-get install nikto                                                           |
| golang        | go lang                                                                        | apt-get install go;add-apt-repository ppa:longsleep/golang-backports; apt-get update |
| gobuster      | gobuster                                                                       | go get github.com/OJ/gobuster                                                        |
+---------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
```
### Get all SQL commands
```

python opsec_auto.py --sql
+SQL Commands--+-------------------------------------------------------------------------------------------------------+-------------------------------------------+
| SQL COMMANDS | command                                                                                               | command_description                       |
+--------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------+
| nmap         | nmap -sV -Pn -vv -script=mysql* $ip -p 3306                                                           | sql vuln scan                             |
| nmap         | ./prog_docs/sql_nmap $ip                                                                              | nmap mysql command                        |
| sqlmap       | ./prog_docs/sql_map                                                                                   | echoe's example usage                     |
| metasploit   | ./prog_docs/bashscripts/mssql_enum_ms.sh $ip                                                          | runs ms-sql scanner in metasploit         |
| bruteforce   | ./prog_docs/bashscripts/mssql_login_ms.sh $ip                                                         | runs metasploits aux brute force programs |
| bruteforce   | ./prog_docs/bashscripts/hydra_bf.sh $ip                                                               | echo's example of usage                   |
| bruteforce   | sqlmap -u 'http://$ip/?query' --data='user=foo&pass=bar&submit=Login' --level=5 --risk=3 --dbms=mysql | sqlmaps for query                         |
+--------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------+
```


### Get all web-app commands
```
python opsec_auto.py --web-app
+Web App Commands--+-------------------------------------------------------------------------------------+-----------------------------------+
| WEB APP COMMANDS | command                                                                             | command_description               |
+------------------+-------------------------------------------------------------------------------------+-----------------------------------+
| scan             | nikto -h $ip                                                                        | runs nikto against target ip      |
| scan             | nikto -h $ip -p 80,8080,1234                                                        | runs nikto on different ports     |
| scan             | nikto -host http://$ip                                                              | runs nikto scan with -host option |
| discover         | wfuzz -c -z file,fastlists/directory-list-2.3-medium.txt --sc 200 http://$ip/FUZZ   | brute force discovery             |
| discover         | gobuster -u http://$ip/ -w fastlists/common.txt -s '200,204,301,302,307,403,500' -e | brute force discovery             |
| discover         | gobuster -u http://$ip/ -w fastlists/CGIs.txt -s '200,204,403,500' -e               | brute force CGI                   |
| discover         | whatweb $ip                                                                         | identifies all known services     |
| nmap             | nmap --script http-methods --script-args http-methods.url-path='/test' $ip          | tests allowed methods             |
| nmap             | nmap --script=http-vuln* $ip                                                        | checks http vulns                 |
| nmap             | nmap -v -p 80 --script=http-vuln-cve2010-2861 $ip                                   | test for coldfusion               |
| nmap             | sudo nmap -sU --script=ms-sql-info $ip                                              | nmap to get info                  |
| bruteforce       | hydra -U http-post-form                                                             | what does module do?              |
| bruteforce       | hydra -l user -P /usr/share/wordlists/rockyou.txt -f $ip http-get /path             | basic get auth                    |
+------------------+-------------------------------------------------------------------------------------+-----------------------------------+
```

# How To Contribute

All commands are now stored in a SQLITE3 database. 

The helper script, `/helpers/add_command.py` will walk you through a wizard on what to do.

When you run the script by executing 'python add_command.py' you will be greeted with the following outputs.


```
Choose a topic

pks => PACKAGES
nmap => NMAP COMMANDS
enum => ENUMERATION SCRIPTS
smtp => SMTP COMMANDS
lists => FASTLISTS
ssl => SSL COMMANDS
rpc => RPC COMMANDS
ssh => SSH SCRIPTS
sql => SQL
ftp => FTP SCRIPTS
nfs => NFS COMMANDS
dns => DNS COMMANDS
shellshock => SHELL SHOCK SCRIPTS
smb => SMB COMMANDS
web_apps => WEBAPP COMMANDS

>> nmap

What's the command?: nmap -p- $ip

What's it do?: finds all ports

Inserted
```
