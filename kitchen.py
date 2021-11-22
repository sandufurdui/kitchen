
import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 1500        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'dining hall up at localhost:500')
    data = s.recv(1024)

print('Received:', repr(data))