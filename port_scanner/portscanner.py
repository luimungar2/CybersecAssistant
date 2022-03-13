#!/usr/bin/python3
"""
@author: Luis Muñiz García
"""

import socket
from tabulate import tabulate
from tqdm import tqdm as tq

class PortScanner:
    """
    This class contains all methods for scanning a port,
    tracking a single service, or take the whole active services table.
    """

    def __init__(self,ip):
        """
        Definition of main common parameters
        args: ip address
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(0.001)
        self.host = ip
        self.port = 80
        self.protocol = ""
        self.pair = []
        #self.list_of_services = []
        self.print_msg_flag = True

    def port_scanner(self,port):
        """
        args: port
        returns: True if port is used, False otherwise.
        """
        self.port = port
        if self.socket.connect_ex((self.host, self.port)):
            if self.print_msg_flag:
                print("The port is closed")
                self.socket.close()
            return False
        else:
            if self.print_msg_flag:
                print("The port is open")
                self.socket.close()
            return True

    def print_service_on_port(self,port,protocol):
        """
        args: port, protocol
        returns: name of the requested service
        """
        self.port = port
        self.pair=[]
        self.protocol=protocol
        if self.port_scanner(self.port):
            self.pair.append(port)
            service_name = socket.getservbyport(self.port, self.protocol)
            print(service_name)
            self.pair.append(service_name)
            if self.print_msg_flag:
                print("Servicio %d en puerto %s"%(self.port, service_name))
            return self.pair
        else:
            if self.print_msg_flag:
                print("No service available on port ",port)
            return self.pair

    def scan_services(self):
        """
        Uses the scan method from scan.py.
        For some reason, it does not works properly
        when it is implemented on this class.
        """
        services = []
        print("Escaneando...")
        for i in tq(range(0, 65536)):
            service = None
            try:
                service = socket.getservbyport(i)
            except Exception as exception:
                print(exception)
            if service is not None:
                services += [{'service': service, 'port': i}]
        print("Listo! imprimiendo tabla de servicios activos:")
        print(tabulate(services))
        # for idx, s in enumerate(services):
        #     print(idx, " port nr ", s['port'], " runs service ", s['service'])

if __name__ == "__main__":
    IP = "127.0.0.1"
    escaneo = PortScanner(IP)
    #escaneo.port_scanner(port)
    escaneo.print_msg_flag = False
    #escaneo.scan_services()
    escaneo.scan_services()
