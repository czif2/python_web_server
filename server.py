from socket import *

# 创建一个基于IPv4和TCP协议的Socket：
serverSocket = socket(AF_INET, SOCK_STREAM)
# 指定了套接字与端口号6789绑定
serverSocket.bind(('', 6789))
# 指定了服务器在同一时刻只接受一个请求
serverSocket.listen(1)
# 服务器程序通过一个永久循环来接受来自客户端的连接
while True:
    print('服务器已就位')

    # accept() 会等待并返回一个客户端的连接:建立连接
    connectionSocket, addr = serverSocket.accept()
    try:
        # recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环
        # 要将bytes字符串转换为Unicode文本str字符串，您必须知道该字符串是用什么字符集编码的，因此您可以调用decode
        message = connectionSocket.recv(1024).decode()
        print(message)
        # 这里split('.')[1]是一种缩写形式，把它拆开来看实际就是先用split('.')方法将字符串以"."开割形成一个字符串数组，
        # 然后再通过索引[1]取出所得数组中的第二个元素的值
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:], encoding='utf-8')
        print(f)
        outputdata = f.read()
        print(outputdata)
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata)+24)
        connectionSocket.send(header.encode())
        print(header.encode())
        for i in range(0, len(outputdata)):

            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # connectionSocket.close()
    except IOError:
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        # connectionSocket.close()
