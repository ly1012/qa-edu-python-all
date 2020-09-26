# -*- encoding=utf-8 -*-

import socket

def server():
    # 创建 socket
    s = socket.socket()
    host = '127.0.0.1'
    port = 6666

    # 绑定套接字
    s.bind((host, port))

    # 监听
    s.listen(5)

    while True:
        # 等待连接建立
        c, addr = s.accept()
        # 打印已建立连接的地址（发送方套接字）
        print('Connect Addr: ', addr)
        # 接受客户端发送过来的消息
        print('Msg from client: ', c.recv(1024).decode('utf-8'))
        # 发送消息给客户端
        c.send(b'Server Msg')
        c.close()

if __name__ == '__main__':
    server()