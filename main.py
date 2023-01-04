from Assistant.assistant import *
from scanner.nmap import Scanner

class CyberAssistant(Assistant):
	"""
	Experimental Class using Assistant and Scanner
	"""
	def __init__(self):
		super(CyberAssistant, self).__init__()
		self.ip = "127.0.0.1"
		self.file = "ejemplo.txt"
		self.scanner = Scanner(self.ip, self.file)
		
	def start_scan(self):
		self.scanner.scan_services()
		return True
	
	def read_results(self):
		self.scanner.analyze_results()
		cadena_ejemplo = "Abierto el puerto 80. Posible servidor HTTP."
		return cadena_ejemplo

if __name__ == "__main__":
	assistant = CyberAssistant()
	assistant.speaks("iniciando escaneo")
	assistant.start_scan()
	resultados = assistant.read_results()
	assistant.speaks("Abierto el puerto 80. Posible servidor HTTP.")


	