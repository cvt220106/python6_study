# @Author : 杨佳杰
# @Time   : 2022/6/16 10:09
# @File   : 2-tcp服务器端.py
from socket import *
import select
import sys

chat_server = socket(AF_INET, SOCK_STREAM)  # ipv4,TCP
# ip地址+端口号(port)--连接确定的网络进程
server_arr = ('192.168.85.128', 2000)
# 服务器端与IP地址以及端口建立连接
chat_server.bind(server_arr)
# 开始倾听客户端的连接请求
chat_server.listen(10)  # int值为tcp服务器缓冲区大小!

epoll = select.epoll()
# epoll检测对象
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(chat_server.fileno(), select.EPOLLIN)

client_socket = None
while True:
    events = epoll.poll(-1, 3)
    # -1标识永久监测等待,2代表目前有两个目标需要监测!返回值events为一个元祖元素的列表
    # 元祖内容为文件标识符与事件
    for fd, event in events:
        if fd == chat_server.fileno():
            # 有客户端连接上
            client_socket, _ = chat_server.accept()  # 获取客户端通信所用的套接字
            # 为该客户注册epoll
            epoll.register(client_socket.fileno(), select.EPOLLIN)
        elif fd == sys.stdin.fileno():  # 代表标准输入里边有数据
            data = input('请输入数据:')
            if not client_socket:
                # 客户端未连接时,不发送数据
                print('客户端还未连接!')
                continue
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno():  # 代表接收缓冲区内有数据
            recv_data = client_socket.recv(100)
            if not recv_data:
                print('对方断开了!')
                #断开后,关闭对客户端epoll的检测
                epoll.unregister(client_socket.fileno())
                client_socket.close()
                continue
            print(recv_data.decode('utf8'))

client_socket.close()
chat_server.close()