import sqlite3
from colorama import init, Fore, Back, Style
init(autoreset=True)


def cy_on_ma(string):
    return Style.BRIGHT + Fore.CYAN + string + Fore.RESET + Style.RESET_ALL

def green(string):
    return Style.BRIGHT + Fore.GREEN + string + Fore.RESET + Style.RESET_ALL


def insert_into_db(topic, command, description):
    conn = sqlite3.connect("offsec.db")
    conn.execute('INSERT INTO commands (topic, command, description, mod_name) VALUES (?,?,?,?)', (topic, cy_on_ma(command), green(description), topic))
    conn.commit()
    conn.close()



all_commands = {"sql":"SQL",
        "pks":"PACKAGES",
        "lists":"FASTLISTS",
        "nmap":"NMAP COMMANDS",
        "dns":"DNS COMMANDS",
        "smb":"SMB COMMANDS",
        "nfs":"NFS COMMANDS",
        "enum":"ENUMERATION SCRIPTS",
        "ssh":"SSH SCRIPTS",
        "ftp":"FTP SCRIPTS",
        "ssl":"SSL COMMANDS",
        "smtp":"SMTP COMMANDS",
        "rpc":"RPC COMMANDS",
        "web_apps":"WEBAPP COMMANDS",
        "shellshock": "SHELL SHOCK SCRIPTS",
        "hc":"HELPER_COMMANDS"}

def main():
    string = 'Choose a topic\n'
    for key, val in all_commands.iteritems():
        string += key + " => " + val + "\n"
    string += ">> "
    topic = raw_input(string)
    command = raw_input("What's the command?: ")
    description = raw_input("What's it do?: ")
    insert_into_db(topic, command, description)
    exit("Inserted")


if __name__ == "__main__":
    main()










