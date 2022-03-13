from Assistant.assistant import *
from port_scanner.portscanner import *

class ScannerAssistant(Assistant,PortScanner):
	"""
	Experimental Class using Assistant and PortScanner
	"""
	def __init__(self):
		super(ScannerAssistant, self).__init__()
		PortScanner.__init__(self,"127.0.0.1")
		self.host = "127.0.0.1"

if __name__ == "__main__":
	new_scan_assistant= ScannerAssistant()
	new_scan_assistant.speaks("Escaneando puerto 80")
	if new_scan_assistant.port_scanner(80):
		new_scan_assistant.speaks("Puerto abierto.")
	
