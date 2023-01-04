#!/usr/bin/python3
"""
@author: Luis Muñiz García
"""

#from tabulate import tabulate
#from tqdm import tqdm as tq
import os 

class PortScanner:
    """
    This class contains all methods for scanning a port,
    tracking a single service, or take the whole active services table.
    """

    def __init__(self,ip,filename):
        """
        Definition of main common parameters
        args: ip address, output file name
        """
        self.host = ip
        self.file = filename

    def scan_services(self):
        """
        Uses the nmap tool.
        """
        try:
            os.system("nmap -A -T4 -v -sV -sC "+self.host+" > "+self.file)
            return True
        except Exception as scan_err:
            print("Error while scanning: "+str(scan_err))
            return False
    
    def analyze_results(self):
        """
        Reads the results.
        """
        try:
            f = open(self.file,'r')
            print(f.read())
            return True
        except Exception as analyze_err:
            print("Error while analyzing: "+str(analyze_err))
            return False


if __name__ == "__main__":
    IP = "10.129.16.98"
    NOMBRE_FICHERO = "resultado_escaneo.txt"
    escaneo = PortScanner(IP,NOMBRE_FICHERO)
    escaneo.scan_services()
    escaneo.analyze_results()