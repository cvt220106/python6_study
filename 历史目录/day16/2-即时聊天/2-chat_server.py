# @Author : 杨佳杰
# @Time   : 2022/6/16 10:09
# @File   : 2-tcp服务器端.py
from socket import *
import select
import sys

chat_server = socket(AF_INET, SOCK_STREAM)  # ipv4,TCP
# ip地址+端口号(port)--连接确定的网络进程
server_arr = ('10.207.39.89', 2000)
# 服务器端与IP地址以及端口建立连接
chat_server.bind(server_arr)
# 开始倾听客户端的连接请求
chat_server.listen(10)  # int值为tcp服务器缓冲区大小!

# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server就可以省下来专门等待其他新客户端的链接
client_socket, client_addr = chat_server.accept()

epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 标准输入监测
epoll.register(client_socket.fileno(), select.EPOLLIN)  # 接收缓冲区监测

while True:
    events = epoll.poll(-1, 2)
    # -1标识永久监测等待,2代表目前有两个目标需要监测!返回值events为一个元祖元素的列表
    # 元祖内容为文件标识符与事件
    for fd, event in events:
        if fd == sys.stdin.fileno():  # 代表标准输入里边有数据
            data = input('请输入数据:')
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno():  # 代表接收缓冲池内有数据
            recv_data = client_socket.recv(100)
            if not recv_data:
                print('对方断开了!')
                exit()
            print(recv_data.decode('utf8'))

