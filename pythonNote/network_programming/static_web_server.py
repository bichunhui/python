import socket
import re
import sys
from multiprocessing import Process

HTML_ROOT_DIR = "./html"
WSGI_PYTHON_DIR = "./wsgipython"

class HTTPServer(object):
	def __init__(self):
		self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	def start_response(self,status,headers):
		"""
			 status = "200 OK"
		headers = [
			("Content-Type", "text/plain")
		]
		"""
		response_headers = "HTTP/1.1" + status + "\r\n"
		for header in headers:
			response_headers += "{}: {}\r\n".format(header[0],header[1])
		self.response_headers = response_headers

	def dealClientRequest(self,clientSocket):
		recvData = clientSocket.recv(1024).decode("utf-8") #接收到就可以直接解码
		print('{}'.format(recvData))
		recvList = recvData.splitlines()
		for request in recvList:
			print(request)
		request_start_line = recvList[0]
		# 'GET / HTTP/1.1'
		request_dir = re.match(r"\w+ +(/[^ ]*) ",request_start_line).group(1)  #匹配时一定要group(1)
		method = re.match(r"(\w+) +/[^ ]* ",request_start_line).group(1)  #匹配时一定要group(1)
		if request_dir.endswith(".py"):
			try:
				m = __import__(request_dir[1:-3])
			except Exception:
				self.response_headers = "HTTP/1.1 404 Not Found\r\n"
				self.response_body = "not found"
			else:
				env = {
				"PATH_INFO": request_dir,
				"METHOD": method
				}
				response_body = m.application(env,self.start_response)
			response = self.response_headers + "\r\n" + response_body

		else:
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
	sys.path.insert(1,WSGI_PYTHON_DIR)
	httpServer = HTTPServer()
	httpServer.bind(8000)
	httpServer.createProcess()
	serverSocket.close()

if __name__ == "__main__":
	main()
