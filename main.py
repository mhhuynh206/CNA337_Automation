# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020
# Mychael Huynh 12/10/2020
# Got help from Hasan

from Server import Server
def print_program_info():

    print("Server Automator v0.1 by Mychael")

if __name__ == '__main__':
    print_program_info()

    EC2server = Server('18.216.116.156')

    print(EC2server.ping())
