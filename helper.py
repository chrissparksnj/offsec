import sqlite3
import prog_docs.text_content as txt

wa = txt.web_app_commands
sql = txt.sql_commands
pks = txt.git_commands
lists = txt.fastlists
nmap = txt.nmap
dns = txt.dns
smb = txt.smb
nfs = txt.nfs_commands
enum = txt.enum_scripts
ssh = txt.ssh_commands
ftp = txt.ftp_commands
ssl = txt.ssl
smtp = txt.smtp_commands
rpc = txt.rpc

all_commands = {"sql":sql, "pks":pks, "lists":lists, "nmap":nmap, "dns":dns, "smb":smb, "nfs":nfs, "enum":enum, "ssh":ssh, "ftp":ftp, "ssl":ssl, "smtp":smtp, "rpc":rpc}

def extract(l, m):
    for l1 in l:
        try:
            topic = l1[0]
            if "COMMANDS" in topic:
                pass
            else:
                command = l1[1].replace("\x1b[33m", "")
                description = l1[2]
                insert_into_db(topic, command, description, m)
        except:
            print "Couldnt enter: " + str(command)

def insert_into_db(topic, command, description, mod_name):
    conn = sqlite3.connect("offsec.db")
    conn.execute('INSERT INTO commands (topic, command, description, mod_name) VALUES (?,?,?, ?)', (topic, command, description, mod_name))
    conn.commit()
    conn.close()


def main():
    for key, val in all_commands.iteritems():
        extract(val, key)

if __name__ == "__main__":
    main()










