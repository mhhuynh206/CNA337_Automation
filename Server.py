import os
class Server:
    """ Server class for representing and manipulating servers. """
    def __init__(self, server_ip):

        self.server_ip = server_ip
    def ping(self):

        response = os.system("ping -n 4 " +self.server_ip)
        return self.server_ip

# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020
# Mychael Huynh 12/10/2020
# Got help from Hasan

import paramiko
user_name = "ubuntu"
passwd = ""
ip = "18.216.116.156"
Private_key = r"mychaelplswork"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=ip, username=user_name, password=passwd,key_filename=Private_key)

stdin, stdout, stderr = ssh.exec_command('''sudo apt-get update
                                         sudo apt-get upgrade -y
                                         ''')
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print (line)


ssh.close()