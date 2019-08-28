## Pentesting Notes and Commands

### Install Instructions
`git clone https://github.com/chrissparksnj/offsec.git`

`cd offsec/`

`source venv/bin/activate`

`pip install -r requirements.txt`



### Running Program
```
$ python opsec_auto.py -h

usage: opsec_auto.py [-h] [-hc] [-pk] [-gc] [-gm] [-ul] [-it] [-nc]
                     [-c {nmap_100,nmap_all,nmap_udp,nmap_dns,nmap_smb_ports,nmap_brute}]
                     [--crt-search] [--flush-db] [--subdomains] [--raw-ip]
                     [--domain DOMAIN] [--version]

Automatically spin up everything from the guide.offsecnewbie.com walk through

optional arguments:
  -h, --help            show this help message and exit
  -hc, --helper-commands
                        show helper commands
  -pk, --packages       Show interesting packages and their install
                        instructions
  -gc, --get-commands   shows all commands offered within the tutorial
  -gm, --get-modules    shows methodology offered within the tutorial
  -ul, --useful-links   shows useful link
  -it                   Install a standardized template to your home directory
  -nc                   Show all networking commands
  -c {nmap_100,nmap_all,nmap_udp,nmap_dns,nmap_smb_ports,nmap_brute}
                        run a command with the shortcode
  --crt-search          use crt.sh to find subdomains
  --flush-db            flush the recon-ng database
  --subdomains          use recon-ng to get a list of subdomains
  --raw-ip              Get raw ip addresses of subdomains
  --domain DOMAIN       the target domain
  --version             show program's version number and exit
```


### Example Usage

```
-pk, --packages shows list of pentesting packages
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
