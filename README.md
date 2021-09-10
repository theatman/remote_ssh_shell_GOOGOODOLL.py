<h1>Goo Goo Doll Remote SSH Shell</h1>
<h2>Shell to access SSH servers and run remote commands.</h2>
<b>Goo Goo Doll Remote SSH Shell - remote_ssh_shell_GOOGOODOLL.py (Version 1.0 July 2021)</b>

<h2>Purpose</h2>
This script can allow you to send common commands to an SSH remote server such as:
whoami, id, ls, pwd, cat (as in cat /etc/passwd), wget, rm, cp, mv, ls -la, curl (and many more). 
You can't change directories, but you can do something like this if you know the file exists:
$ cat /home/tom/Documents/file-you-knew-existed.txt

IMPORTANT: Credentials for the remote server you're trying to connect to are necessary to run this script.

<h2>Getting Started</h2>
You can add the IP address of the SSH server you're trying to connect to/attack and the username in the script's line 55.
Once you execute the script, you will be prompted to enter the acount's password.
<br>
<p>To run:
<p>$ python3 remote_ssh_shell_GOOGOODOLL.py</p>
<p>To end session type "quit" or hit Ctrl-C </p>
<br>
<p>Modules you'll need to pip install:</p>
<p>getpass</p> 
<p>threading</p>
<p>paramiko</p>
<p>subprocess</p>

<h3>Questions</h3>
Questions? dolores@infosecpath.com

DISCLAIMER: This is meant to be for educational and/or pentesting purposes only.
