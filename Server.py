import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        """ Create a ServerClass with a server_ip instantiated"""
        self.server_ip = server_ip

    def ping(self):
        response = os.system("ping -c 1 -W 5 " + self.server_ip + " > /dev/null 2>&1")
        
        # if command response is 0, then server is up and running
        if response == 0:
            return (self.server_ip + "is Up and Running")
        
        #else the server is not running and down
        else:
            return (self.server_ip + " is Down")
