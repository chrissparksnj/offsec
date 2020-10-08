#!/usr/bin/python2.7
from optparse import OptionParser
import socket
import sys


parser = OptionParser()
parser.add_option("-p", "--port", type='int', action="store", dest="port", help="specify a port", default=25)
parser.add_option("-i", "--host", type='string', action="store", dest="host", help="specify a host")
parser.add_option("-t", "--timeout", type="int", action="store", dest="time", help="set timeout for connection", default=5)
parser.add_option("-u", "--user", type="string", action="store", dest="user", help="specifies user", default="root")
(options, args) = parser.parse_args()
print "-----------"
print "Banner grabbing and user check for SMTP"
print "-----------"
print "Host: " + options.host
print "Port: " + str(options.port)
print "Timeout: " + str(options.time)
print "User: " + options.user
print "-----------"
# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the Server
s.settimeout(options.time)
print("Connecting to server")
try:
    connect = s.connect((options.host, options.port))
except:
    print("Could not connect to server. Try increasing timeout (-t) or something else.")
    exit(0)
print("Connected: grabbing banner")
# Receive the banner
banner = s.recv(1024)
print banner
# VRFY a user
s.send('VRFY ' + options.user + '\r\n')
result = s.recv(1024)
print result
# Close the socket
s.close()

