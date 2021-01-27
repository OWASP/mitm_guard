#!/bin/bash
# Script to add a user to Linux system
if [ $(id -u) -eq 0 ]; then
  username="user_agent"
	password="1368-box"
	egrep "^$username" /etc/passwd >/dev/null
	if [ $? -eq 0 ]; then
		exit 1
	else
		pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
		useradd -m -p $pass $username
		usermod -aG wheel $username
		[ $? -eq 0 ] || echo "Failed to add a user!"
	fi
else
	echo "Only root may add a user to the system"
	exit 2
fi
