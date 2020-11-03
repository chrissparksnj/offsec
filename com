#!/usr/bin/python2
import os
import sqlite3
from colorama import init, Fore, Back, Style
init(autoreset=True)


def cy_on_ma(string):
    return Style.BRIGHT + Fore.CYAN + string + Fore.RESET + Style.RESET_ALL

def green(string):
    return Style.BRIGHT + Fore.GREEN + string + Fore.RESET + Style.RESET_ALL


def insert_into_db(topic, command, description):
    curdir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(curdir + '/offsec.db')
    conn.execute('INSERT INTO commands (topic, command, description, mod_name) VALUES (?,?,?,?)', (topic, cy_on_ma(command), green(description), topic))
    conn.commit()
    conn.close()

def insert_port(pn, sn, sd):
    #(id INTEGER PRIMARY KEY AUTOINCREMENT, portnumber text, servicename text, service description text);
    curdir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(curdir + '/offsec.db')
    conn.execute("INSERT into ports (portnumber, servicename, servicedescription) VALUES (?,?,?)", (cy_on_ma(pn), green(sn), sd))
    conn.commit()
    conn.close()



all_commands = {"sql":"SQL",
        #"pks":"PACKAGES",
        #"lists":"FASTLISTS",
        #"nmap":"NMAP COMMANDS",
        "dns_ha":"DNS COMMANDS",
        "smtp_ha":"SMTP COMMANDS",
        "ig":"IG COMMANDS",
        "port":"PORT INFO",
        #"smb":"SMB COMMANDS",
        #"nfs":"NFS COMMANDS",
        #"enum":"ENUMERATION SCRIPTS",
        #"ssh":"SSH SCRIPTS",
        #"ftp":"FTP SCRIPTS",
        #"ssl":"SSL COMMANDS",
        #"smtp":"SMTP COMMANDS",
        #"rpc":"RPC COMMANDS",
        #"web_apps":"WEBAPP COMMANDS",
        #"shellshock": "SHELL SHOCK SCRIPTS",
        #"hc":"HELPER_COMMANDS"
        }
def runcommands():
    string = ''
    for key, val in all_commands.iteritems():
        string += key + " => " + val + "\n"
 
    string += "Whats the topic?: "
    topic = raw_input(string)
    command = raw_input("What's the command?: ")
    description = raw_input("What's it do?: ")
    insert_into_db(topic, command, description)
    exit("Inserted")

def runports():
    string = "Whats the port number?: "
    port = raw_input(string)
    servicename  = raw_input("What's the service called?: ")
    servicedescription = raw_input("What's the description of service?: ")
    insert_port(port, servicename, servicedescription)
    exit("Inserted")



def main():
    t = raw_input("Insert port(p) or command(c) ?:")
    if t == "p":
        runports()
    if t == "c":
        runcommands()


if __name__ == "__main__":
    main()










