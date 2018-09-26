import sys
import time
import gevent

from gevent import socket monkey
monkey.patch_all()


def handle_request(conn):
	while True:
		data = conn.recv(1024)
		if not data:
			conn.close()
			break
		print("recv:",data)
		conn.send(data)

def server(port):
	s = socket.socket()
	s.bind(("",port))
	s.listen(s)
	while True:
		cli,addr = s.accept()
		gevent.spawn(handle_request,cli)
