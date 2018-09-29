import socket
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"
class HTTPServer(object):
	def __init__(self):
		self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	def dealClientRequest(self,clientSocket):
		recvData = clientSocket.recv(1024).decode("utf-8") #接收到就可以直接解码
		print('{}'.format(recvData))
		recvList = recvData.splitlines()
		for request in recvList:
			print(request)
		request_start_line = recvList[0]
		# 'GET / HTTP/1.1'
		request_dir = re.match(r"\w+ +(/[^ ]*) ",request_start_line).group(1)  #匹配时一定要group(1)
		if request_dir == "/":
			request_dir = "/index.html"
		try:
			file = open(HTML_ROOT_DIR+request_dir,"rb") #不加双引号
		except IOError:
			response_start_line = "HTTP/1.1 404 Not Found!\r\n"
			response_headers = "Server: My server\r\n"
			response_body = "The file is not found!"
		else:
			file_data = file.read()
			file.close()
			response_start_line = "HTTP/1.1 200 OK\r\n"
			response_headers = "Server: My server\r\n"
			response_body = file_data.decode("utf-8")  #需要解码
		response = response_start_line + response_headers + "\r\n" + response_body
		print('{}'.format(response))
		clientSocket.send(response.encode("utf-8"))   #在发送的时候需要编码
		clientSocket.close()
	def createProcess(self):
		self.serverSocket.listen(5)
		while True:
			clientSocket,clientInfo = self.serverSocket.accept()
			print('{}:{}用户已经连接'.format(clientInfo[0],clientInfo[1]))
			process = Process(target=self.dealClientRequest,args=(clientSocket,))
			process.start()
			clientSocket.close()

	def bind(self,port):
		self.serverSocket.bind(("",port))

def main():
	httpServer = HTTPServer()
	httpServer.bind(8000)
	httpServer.createProcess()
	serverSocket.close()

if __name__ == "__main__":
	main()
