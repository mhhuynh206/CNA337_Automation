import os
class Server:
    """ Server class for representing and manipulating servers. """
    def __init__(self, server_ip):

        self.server_ip = server_ip
    def ping(self):

        response = os.system("ping -n 4 " +self.server_ip)
        return self.server_ip
