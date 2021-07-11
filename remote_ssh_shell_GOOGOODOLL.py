#!/usr/bin/env python3
#
# remote_ssh_shell_GOOGOODOLL.py  (Version 1.0 - July 2021)
# SSH Client to run remote commands
#
# Questions to: dolores@infosecpath.com
# Lots of this code received the immense collaboration of a great Python wizard friend of mine.
#
# This script can allow you to send common commands to an SSH remote server such as:
# whoami, id, ls, pwd, cat (as in cat /etc/passwd), wget, rm, cp, mv, ls -la, curl (and many more). 
# You can't change directories, but you can do something like this if you know the file exists:
# cat /home/tom/Documents/sample.txt

# IMPORTANT: Credentials for the remote server you're trying to connect to are necessary to run this script.

# HOW TO USE:
# You can add the IP address of the SSH server you're trying to connect to on Line 55.
# You can add the SSH username on Line 55.
# You will need to enter the password, but after running this script!!!
# To run:
# $ python3 remote_ssh_shell_GOOGOODOLL.py
# To end session type "quit" or hit Ctrl-C


import getpass 
import paramiko
import subprocess
import threading


def paramiko_get_client(ip, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    return client


def run_paramiko_shell(client):
    try:
        command = ""
        while command != "quit":
            ssh_session = client.get_transport().open_session()
            if not ssh_session.active:
                print("could not create a session")
            command = input("Type command to execute: ")
            ssh_session.exec_command(command)
            info = ssh_session.recv(1024)
            decoded_info = info.decode('utf-8')
            print (decoded_info) 
    finally: 
        client.close()


def main():
    password = getpass.getpass(prompt="SSH User Password: ") # Don't change anything on this line. You will be able to enter the password after execution.
    client = paramiko_get_client('192.0.0.0', 'username', password) # DO CHANGE the IP address and add the SSH username.
    run_paramiko_shell(client)

if __name__ == "__main__":
    main()
    
# If you enter the correct IP address, username, and password you will not get any errors. 
# That's all folks! Improvements welcomed!

