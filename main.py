# This is the template code for the CNA337 Final Project
# Mychael Huynh
# CNA 337 Fall 2020
# Received help from Hasan

from Server import Server
def print_program_info():

    print("Server Automator v0.1 by Mychael")

if __name__ == '__main__':
    print_program_info()

    EC2server = Server('18.221.253.11')

    print(EC2server.ping())
