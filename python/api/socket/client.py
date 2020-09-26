# -*- encoding=utf-8 -*-

import socket

def client(i):
    # 创建 socket
    s = socket.socket()

    # 连接
    s.connect(('127.0.0.1', 6666))
    port = s.getsockname()[1]

    # 发送消息给服务端
    s.send(str("客户端端口: "+str(port)).encode('utf-8'))
    # 接收服务端的消息
    print('Recv msg: %s, Client: %d' %(s.recv(1024), i))
    s.close()

if __name__ == '__main__':
    for i in range(10):
        client(i)