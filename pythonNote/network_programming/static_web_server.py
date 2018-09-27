import socket
from multiprocessing import Process

def dealClientRequest(clientSocket):
	recvData = clientSocket.recv(1024)
	print('{}'.format(recvData))
	response_start_line = "HTTP/1.1 200 OK\r\n"
	response_headers = "Server: My server\r\n"
	response_body = "hello fanjiale!"
	response = response_start_line + response_headers + "\r\n" + response_body
	print('{}'.format(response))
	clientSocket.send(response.encode("utf-8"))
	# clientSocket.close()
def createProcess(serverSocket):
	while True:
		clientSocket,clientInfo = serverSocket.accept()
		print('{}:{}用户已经连接'.format(clientInfo[0],clientInfo[1]))
		process = Process(target=dealClientRequest,args=(clientSocket,))
		process.start()
		clientSocket.close()

def main():
	serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.bind(("",9000))
	serverSocket.listen(5)
	createProcess(serverSocket)
	serverSocket.close()

if __name__ == "__main__":
	main()
