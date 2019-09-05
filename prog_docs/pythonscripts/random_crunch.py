import sys, os, string, random

''' 
~ used to make random hashes in the form of:
~ ba2d32943ffd0731f3acdb621eg3f22e
'''

if len(sys.argv) < 2:
    print "Please enter a range: eg 100, 200"
hash_count = sys.argv[1]

for i in range(int(hash_count)):
    print ''.join(random.choice('abcdefg' + string.digits) for __ in range(int(32)))



