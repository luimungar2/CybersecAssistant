#!/usr/bin/python3
"""
@author: Luis Muñiz García
"""

import os


class Discover:
    """ This class contains all methods for discover hosts,
    given an ip subnet, and store it into a file. """

    def __init__(self, ip_subnet, mask, filename):
        """ Definition of main common parameters
        args: ip address, output file name """

        self.subnet = ip_subnet
        self.mask = mask
        self.file = filename

    def discover(self):
        ''' Invokes the netdiscover command '''
        try:
            os.system("netdiscover -P -r "+self.subnet+self.mask+" > "+self.file)
            return True
        except Exception as scan_err:
            print("Error while discovering: "+str(scan_err))
            return False

    def analyze_results(self):
        """
        Reads the results.
        """
        try:
            f = open(self.file, 'r')
            print(f.read())
            return True
        except Exception as analyze_err:
            print("Error while analyzing: "+str(analyze_err))
            return False


if __name__ == "__main__":
    IP = "192.168.226.0"
    MASK = "/24"
    NOMBRE_FICHERO = "resultado_discover.txt"
    descubre = Discover(IP, MASK, NOMBRE_FICHERO)
    descubre.discover()
    descubre.analyze_results()
