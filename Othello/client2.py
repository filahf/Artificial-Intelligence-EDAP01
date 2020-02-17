

import socket  # import socket module

s = socket.socket()  # create a socket object
host = 'vm33.cs.lth.se'  # Host i.p
port = 9035  # Reserve a port for your service

s.connect((host, port))
print(s.recv(1024))
s.close
