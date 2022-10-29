from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 6789))
while True:
    header = 'GET /test.html HTTP/1.1\nHost: localhost:6789\nConnection: keep-alive\nUser-Agent: Mozilla/5.0\n\n'
    clientSocket.send(header.encode())
    message = clientSocket.recv(1024)
    print(message.decode())
