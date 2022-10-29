from socket import *
import threading


def tcp_process(connectionSocket):
    print(threading.current_thread())
    try:
        message = connectionSocket.recv(1024).decode()
        print(repr(message))
        print(message)
        filename = message.split()[1]
        f = open(filename[1:], encoding='utf-8')
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata)+24)
        connectionSocket.send(header.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        connectionSocket.close()


if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 6789))
    serverSocket.listen(10)
    while True:
        print('服务器已就位')
        connectionSocket, addr = serverSocket.accept()
        thread = threading.Thread(target=tcp_process, args=(connectionSocket, ))
        thread.start()
