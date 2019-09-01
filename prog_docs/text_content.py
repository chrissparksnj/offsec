from termcolor import colored

commands = [
    "script $target.log-->logs all commands of the current session to the $target.log file",
    "shift Print Screen-->create a screenshot of the selected area and save it",
    "export ip=target_ip-->set the environment variable to a target ip. ex - export ip=192.168.1.1",
]



def wrap_in_green(text):
    return "\033[1;32;40m" + text + "\033[0m"


def c(text):
    return colored(text, 'yellow')

web_app_commands = [
    [wrap_in_green("WEB APP COMMANDS"), "command", "command_description"],
    ["scan", c("nikto -h $ip"), "runs nikto against target ip"],
    ["scan", c("nikto -h $ip -p 80,8080,1234"), "runs nikto on different ports"],
    ["scan", c("nikto -host http://$ip"), "runs nikto scan with -host option"],
    ["discover", c("wfuzz -c -z file,fastlists/directory-list-2.3-medium.txt --sc 200 http://$ip/FUZZ"), "brute force discovery"],
    ["discover", c("gobuster -u http://$ip/ -w fastlists/common.txt -s '200,204,301,302,307,403,500' -e"), "brute force discovery"],
    ["discover", c("gobuster -u http://$ip/ -w fastlists/CGIs.txt -s '200,204,403,500' -e"), "brute force CGI"],
    ["discover", c("whatweb $ip"), "identifies all known services"],
    ["nmap", c("nmap --script http-methods --script-args http-methods.url-path='/test' $ip"), "tests allowed methods"],
    ["nmap", c("nmap --script=http-vuln* $ip "), "checks http vulns"],
    ["nmap", c("nmap -v -p 80 --script=http-vuln-cve2010-2861 $ip"), "test for coldfusion"],
    ["nmap", c("sudo nmap -sU --script=ms-sql-info $ip"), "nmap to get info"],
    ['bruteforce', c('hydra -U http-post-form'), "what does module do?"],
    ["bruteforce", c("hydra -l user -P /usr/share/wordlists/rockyou.txt -f $ip http-get /path"), "basic get auth"]
]

sql_commands = [
    [wrap_in_green("SQL COMMANDS"), "command", "command_description"],
    ["nmap", c("nmap -sV -Pn -vv -script=mysql* $ip -p 3306"), "sql vuln scan"],
    ["nmap", c("./prog_docs/sql_nmap $ip"), "nmap mysql command"],
    ["sqlmap", c("./prog_docs/sql_map"), "echoe's example usage"],
    ["metasploit", c("./prog_docs/bashscripts/mssql_enum_ms.sh $ip"), "runs ms-sql scanner in metasploit"],
    ["bruteforce", c("./prog_docs/bashscripts/mssql_login_ms.sh $ip"), "runs metasploits aux brute force programs"],
    ["bruteforce", c("./prog_docs/bashscripts/hydra_bf.sh $ip"), "echo's example of usage"],
    ["bruteforce",c("sqlmap -u 'http://$ip/?query' --data='user=foo&pass=bar&submit=Login' --level=5 --risk=3 --dbms=mysql"), "sqlmaps for query"],

]


git_commands = [
    ['program name', 'program link', 'program_instructions'],
    ["enum4linux", c("https://github.com/portcullislabs/enum4linux"), "apt install smbclient; git clone; ./enum4linux"],
    ['the_harvester', c('https://github.com/laramies/theHarvester.git'), 'python3 -m pip install -r requirements.txt'],
    ['recon-ng', c('https://github.com/lanmaster53/recon-ng.git'), 'pip install -r REQUIREMENTS'],
    ['wfuzz', c('https://github.com/xmendez/wfuzz.git'), 'python setup.py install'],
    ['shocker', c('https://github.com/nccgroup/shocker.git'), 'python shocker.py'],
    ['seclist', c('https://github.com/danielmiessler/SecLists.git'), 'nothing'],
    ["wfuzz", c("https://github.com/xmendez/wfuzz.git"),
     "sudo apt-get install wfuzz libcurl4-openssl-dev libssl-dev; pip install pycurl"],
    ['searchsploit', c("https://github.com/offensive-security/exploitdb.git"), "wget https://bit.ly/30xEoiM | bash"],
    ['metaploit', c("https://github.com/rapid7/metasploit-framework.git"), 'wget https://bit.ly/32114rF | bash'],
    ["whatweb", c("https://github.com/urbanadventurer/WhatWeb.git"),
     "https://github.com/urbanadventurer/WhatWeb/wiki/Installation"],
    ["dnsrecon", c("https://github.com/darkoperator/dnsrecon.git"), "pip install -r requirements.txt"],
    ["dnsmap.txt", c("https://raw.githubusercontent.com/kkirsche/wordlistgenerator/master/dnsmap.txt"), "wget"],
    ["smbmap", c("https://github.com/ShawnDEvans/smbmap.git"), "git clone; activate; pip3 install -r requirements"],
    ["nmblookup", c("nmblookup"), "apt install samba-common-bin"],
    ["medusa", c("medusa"), "apt-get install medusa"],
    ["nbtscan", c("nbtscan"), "sudo apt-get install nbtscan"],
    ["nikto", c("nikto"), "sudo apt-get install nikto"],
    ["golang", c("go lang"), "apt-get install go;add-apt-repository ppa:longsleep/golang-backports; "],
    ["gobuster", c("gobuster"), "go get github.com/OJ/gobuster"],
    ["proxychains", c("proxychains"), "sudo apt-get install proxychains"],
    ["tor", c("tor"), "sudo apt-get install tor"],
    ["smtp-user-enum", c("git clone https://github.com/pentestmonkey/smtp-user-enum.git"), "enumerates email users"],
    ["nfs-common", c("nfs-common"), "sudo apt install nfs-common"],
    ["whatweb", c("whatweb"), "sudo apt install whatweb"],
    ["onesixtyone", c("onesixtyone"), "sudo apt install onesixtyone"]

    ]

fastlists = [
    ['source', 'name', 'uses'],
    ['https://github.com/thesp0nge/enchant/blob/master/db/directory-list-2.3-medium.txt',
     c('directory-list-2.3-medium.txt'), 'dirbuster'],
    ['https://github.com/danielmiessler/SecLists/master/Discovery/Web-Content/Top1000-RobotsDisallowed.txt',
     c('Top1000-RobotsDisallowed.txt'), 'gobuster'],
    ['https://github.com/rapid7/metasploit-framework/blob/master/data/wordlists/unix_users.txt', c('unix-users.txt'),
     'smtp-user-enum'],
    ["https://svn.nmap.org/nmap/nselib/data/passwords.lst", c("passwords.lst"), "hydra"],
    ["https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt", c("rockyou.txt"), "hydra"]
]

nmap = [
    [wrap_in_green("NMAP COMMANDS"), "command", "command_description"],
    ["nmap", c("nmap -Pn -sC -sV -oA tcp -vv $ip"), "tcp top 1000"],
    ["nmap", c("nmap -Pn -sC -sV -oA all -vv -p- $ip"), "gets all ports for target $ip"],
    ["nmap", c("nmap -Pn -sU --top-ports 100 -oA udp -vv $ip"), "udp top 100"],
    ["nmap", c("locate .nse | grep ftp"), "Find script related to a service your interested in"],
    ["nmap", c("nmap --script-help ftp-anon"), "what does a script do?"]
    ]

dns = [
        [wrap_in_green("DNS COMMANDS"), "command", "description"],
        ["domain", c("whois $ip"), "finds domain names for given ip"],
        ["domain", c("host -t ns $ip"), "finds name servers of host"],
        ["domain", c("host -t mx $ip"), "finds email servers of host"],
        ["domain", c("host -t ns $ip| cut -d ' ' -f 4 #"), "finds domain servers of given ip"],
        ["domain_transfer", c("host -l $ip ns1.$ip"), "request domain transfer"],
        ["domain_transfer", c("dnsrecon -d $ip -t axfr"), "uses dnsrecon to attempt zone transfer"],
        ["subdomain", c("for ip in $(cat list.txt); do host $ip.$website; done"), "takes list of prefixes and attempts to connect"],
        ["subdomain", c("for ip in $(seq 155 190);do host 157.240.18.$ip;done |grep -v 'not found'"), "bash line to brute force target ip address"],
        ["nmap", c("nmap $ip --script=dns-zone-transfer -p 53"), "requests domain transfer"],
        ["domain", c("nslookup $ip"), "runs nslookup on ip address"],
        ["domain", c("host -t ns $ip"), "dns search for misconfigured dns entries"],
        ["domain", c("dnsenum $ip"), "Finds nameservers for a given domain"],
        ["domain", c("python theHarvester.py  -l 500 -b all -d $ip"), "finds subdomains on major search engines"]
    ]

smb = [

    [wrap_in_green("SMB COMMANDS"),"command", "description"],
    [wrap_in_green("NMAP"), "command", "description"],
    ["nmap", c("nmap -sU -sT -p137,138,139,335 $ip"), "runs nmap for common ports of smb"],
    ["nmap", c("nmap -A $ip -p139"), "find SAMBA version number using the SMB OS discovery script"],
    ["nmap", c("sudo nmap -A $ip -p 139"), "use nmap to see version of smb running"],
    ["nmap", c("ls -ls /usr/share/nmap/scripts/smb*"), "shows all nmap scans"],
    ["nmap", c("locate .nse | grep smb"), "locates smb nmap scripts"],
    ["nmap", c("nmap --script=smb-enum* --script-args=unsafe=1 -T5 $ip"), "quick smb enum"],
    ["nmap", c("nmap --script=smb-enum* --script-args=unsafe=1 -T5 $ip"), "quick vuln scan"],
    ["nmap", c("nmap --script=smb-enum* --script-args=unsafe=1 -T5 $ip"), "quick smb enum"],
    ["nmap", c("nmap -p445 --script smb-brute --script-args userdb=$,passdb=$ $ip"),"brute force smb username password with nmap"],
    [wrap_in_green("SMB SCRIPTS"), "", ""],
    ['smb', c('nmblookup -A $ip'), 'tries to communicate with smb port'],
    ["metasploit", c("./prog_docs/smb_version_ms.sh $ip"), "metasploit auxilary module to crack username and password"],
    ["metasploit", c("./prog_docs/smb_multi_ms.sh $ip"), "metasploit multi-exploit"],
    ["bash", c("./prog_files/bashscripts/smb_enum.sh $ip"), "located in /prog_files; SMB Enumeration using nmap"],
    ["bash", c("./prog_files/bashscripts/smb_version.sh $ip"), "located in /prog_files; checks smb version"],
    [wrap_in_green("SMB MAP"), "", ""],
    ["smb", c("enum4linux -a $ip"), "perl script to enumerate names on smb port"],
    ["smb", c("smbmap -H $ip"), "maps out smb ports for given $ip"],
    ["smb", c("smbmap -R $sharename -H $ip"), "recursively list directories"],
    ["smb", c("smbmap -R $sharename -H $ip -A $fileyouwanttodownload -q"), "downloads file in quietmode"],
    ["smb", c("medusa -h $ip -u userhere -P ~/fastlists/10k-most-common.txt -M smbnt")],
    [wrap_in_green("SMB AUXILLARY")],
    ["directive", c("set SMBDirect false"), "Any metasploit exploit through Netbios over TCP in 139, you need to set"],
    ["smbclient", c("smbclient //$ip/share -U username"), "mounts a smb drive with given username"],
    ["smbclient", c("smblclient -N -L \\$ip"), "mounts a smb drive with given username"],
    ["smbclient", c("smbclient //$ip/share "), "anonymous mount; hit enter with blank password"]

]

nfs_commands = [
    [wrap_in_green("NFS COMMANDS"), "command", "description"],
    ["nfs", c("showmount -e $ip"), "shows mounted NFS for given ip"],
    ["nfs", c("mount $ip:/vol/share /mnt/nfs"), "mounts nfs to current working file system"]
]

enum_scripts = [
        [wrap_in_green("ENUMERATION COMMANDS"),"command", "description"],
        ["web", c("smtp-user-enum -M VRFY -U unix_users.txt -t $ip"),"uses pearl script to verify users against MX domain"],
        ["web", c("use auxiliary/scanner/smtp/smtp_enum"), "metasploit module to enumerate email users"],
        ["harvester", c("python theHarvester.py  -l 500 -b all -d $ip"), "runs harvester for subdomains"],
        ["web", c("nmap $ip --script=msrpc-enum"), "uses nmap to enum rpc users"],
        ["web", c("rpcinfo -p $ip"), 'enumerate using rpc'],
        ["ssh", c("./prog_docs/bashscripts/ssh_enum_ms.sh"), "run msfconsole for ssh/enumerate. optional port allowed"],
        ["ssh", c("python 40136.py -U unix_users.txt $ip"), "ssh user enumerator"],
        ["email_enum", c("theharvester -d $ip -b google"), "searches google for emails related to IP"],

    ]

ssh_commands = [
    [wrap_in_green("SSH COMMANDS"),"command", "description"],
    ["ssh", c("hydra -v -V -l root -P password-file.txt $ip ssh"), "bruteforce ssh"],
    ["ssh", c("hydra -v -V -L user.txt -P rockyou.txt -t 16 $ip ssh"), "bruteforce ssh with username list"],
    ["ssh", c("python 40136.py -U unix_users.txt $ip"), "ssh user enumerator"],
    ["ssh", c("./prog_docs/bashscripts/ssh_enum_ms.sh"), "run msfconsole for ssh/enumerate. optional port allowed"],

]

ftp_commands = [
    [wrap_in_green("FTP COMMANDS"), "command", "description"],
    ["ftp", c("--script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor -p1 $ip"),"runs ftp scripts with nmap"],
    ["ftp", c("--script=ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -p21 $ip"),"runs ftp scripts with nmap"],
    ["ftp", c("nmap --script=ftp-* -p 21 $ip"), "runs ftp vulnerability scan"],
    ["ftp", c("hydra -l user -P /usr/share/john/password.lst ftp://$ip:21"), "brute force ftp"],
    ["ftp", c('use auxiliary/scanner/ftp/ftp_login'), "uses metasploit to brute force login"],
    ["tftp", c("nmap -sU -p 69 --script tftp-enum.nse $ip"), "nmap tftp server discovery"],
    ["tftp", c("./prog_docs/bashscripts/tftp_discover_ms.sh"), "metasploit discovery for tftp server"],
	["tftp", c("cat prog_docs/info/tftp_upload.txt"), "tftp instructions on how to upload php shell"],

    ]

ssl = [
    [wrap_in_green("SSL COMMANDS"),"command", "description"],
    ["ssl", c("openssl s_client -connect $ip:443"), "opens ssl connection to ip address"],
    ["ssl", c("nmap --script ssl-enum-ciphers -p 443 $ip"), "check for unsafe ciphers:  Triple-DES and Blowfish"],
    ]

smtp_commands = [
    [wrap_in_green("SMB COMMANDS"),"command", "description"],
    ["web", c("nmap --script=smtp-* -p 25 $ip"), "nmap smtp"],
    ["web", c("hydra -P wordlistsnmap.lst $ip smtp -V"), "hydra for smtp"],
    ["web", c("./prog_docs/bashscripts/test_open_relay.sh"), "tests ip for open relay"],
    ["email_enum", c('./smtp-user-enum.pl -M VRFY -U fastlists/unix_users.txt -t $ip'), "enumerate users with list"],
    ["email_enum", c("./smtp-user-enum.pl -M VRFY -u root -t $ip"), "verifies single user against mailserver"],
    ["email_enum", c("./smtp-user-enum.pl -M VRFY -u root -t $ip"), "ask the server if a user belongs to a mailing list"],
    ["nmap", c("./prog_docs/bashscripts/smtp_vuln_nmap.sh"), "runs nmap scan for all smtp vulns"],
    ["metasploit", c("./prog_docs/bashscripts/smtp_enum_ms.sh"), "uses metasploit aux module to enumerate smtp users"],
    ["hydra", c("hydra -P fastlists/passwords.lst -L fastlists/unix_users.txt $ip smtp -V"), "attempts smtp brute force"],
    ["pop3", c("cat prog_docs/info/pop_3.txt"), "tests server for POP3"]
]

rpc = [
    [wrap_in_green("RPC COMMANDS"),"command", "description"],
    ["nmap", c("nmap -sV -p 111,445 $ip"), "nmap command to detect rpc services"],
    ["nmap", c("nmap $ip --script=msrpc-enum"), "nmap to expose NFS"],
    ["rpc", c("rpcinfo -p $ip"), "shows if any NFS mount exposed"],
    ["metasploit", c("msf > use exploit/windows/dcerpc/ms03_026_dcom"), "use metasploit module"]
]


all_commands = [
    nmap, dns, smb, enum_scripts, ssh_commands, ftp_commands, ssl, smtp_commands
]

useful_links = [
    "http://packetlife.net/media/library/23/common_ports.pdf-->info graphic of common ports running on public servers.",
    "https://makensi.es/stf-->A giant inventory of recon tools is available via the Skip Tracing Framework",
    "https://www.youtube.com/watch?v=jUc1J31DNdw&t=445s-->how to video on smbmap",
]

methods = [
    ["Topic", "Do", "Do", "Do", "Do", "Do"],
    [c("For i in open TCP/UDP port"), "service and version", "known service bugs", "configuration issues", "Run scan / banner grabbing"],
    [c("GoogleFoo"), "URL path and error message", "parameter to find versions/apps/bugs", "Every version exploit db"],
    [c("GoogleFoo"), "Every version vulnerability", "User enumeration"],
    [c("If app has auth"), "User enumeration", "Password bruteforce", "Default credentials google search"],
    [c("If everything fails:"), "nmap --script exploit -Pn $ip"],
    [c("WebApp Service Scans"),  "Nikto", "dirb", "dirbuster", "wpscan", "dotdotpwn/LFI suite"],
    [c("WebApp Service Scans"),"davtest/cadeavar", "droopscan", "joomscan", "LFI\RFI test"],
    [c("Linux\Windows"), "snmpwalk -c public -v1 $ip 1", "smbclient -L //$ip", "smbmap -H $ip", "rpcinfo", "Enum4lLinux"],
    [c("Anything Else"), "nmap scripts", "hydra", "MSF Aux Modules"],
    [c("Exploitation"), "Gather version numbers", "Searchsploit", "Default Creds"],
    [c("Exploitation"), "Creds previously gathered", "Download the software"],
    [c("Post-Exploitation"), "Linux", "linux-local-enum.sh", "linuxprivchecker.py", "linux-exploit-suggestor.sh", "unix-privesc-check.py"],
    [c("Post-Exploitation"), "Windows", "wpc.exe", "windows-exploit-suggestor.py", "windows_privesc_check.py", "windows-privesc-check2.exe"],
    [c("Final"), "Screenshot of IPConfig/WhoamI", "Copy proof.txt", "Dump hashes", "Dump SSH Keys", "Delete files"]

]
