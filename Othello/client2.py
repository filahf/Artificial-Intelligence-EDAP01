
import socket

HOST = 'vm33.cs.lth.se'  # The server's hostname or IP address
PORT = 9035        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))