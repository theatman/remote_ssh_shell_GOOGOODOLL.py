remote_ssh_shell_GOOGOODOLL.py (Version 1.0 July 2021)
Shell to access SSH servers and run remote commands.

Questions? dolores@infosecpath.com

This script can allow you to send common commands to an SSH remote server such as:
whoami, id, ls, pwd, cat (as in cat /etc/passwd), wget, rm, cp, mv, ls -la, curl (and many more). 
You can't change directories, but you can do something like this if you know the file exists:
$ cat /home/tom/Documents/file-you-knew-existed.txt

IMPORTANT: Credentials for the remote server you're trying to connect to are necessary to run this script.

HOW TO USE:
You can add the IP address of the SSH server you're trying to connect to in Line 55.
You can add the SSH username in Line 55.
You will need to enter the password, but after running this script!!!
To run:
$ python3 remote_ssh_shell_GOOGOODOLL.py
To end session type "quit" or hit Ctrl-C

Modules you'll need to pip install:
getpass 
threading
paramiko
subprocess


DISCLAIMER: This is meant to be for educational and/or pentesting purposes only.
