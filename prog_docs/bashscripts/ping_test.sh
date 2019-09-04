#/bin/bash

#used to test for cloudflare domains

domain=$1

strings=( direct. ftp. direct-connect. cpanel. mail.  )
for i in "${strings[@]}"
do
	test_domain="${i}${domain}"
	ping -c 1 $test_domain
done
