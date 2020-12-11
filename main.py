# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020
# Hasan Hasan 11/24/2020

from Server import Server
def print_program_info():

    print("Server Automator v0.1 by Hasan")

if __name__ == '__main__':
    print_program_info()

    EC2server = Server('18.191.53.207')

    print(EC2server.ping())
