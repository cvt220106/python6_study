# @Author : 杨佳杰
# @Time   : 2022/6/16 10:01
# @File   : 1-tcp客户端.py
from socket import *
import select
import sys

chat_client = socket(AF_INET, SOCK_STREAM)  # ipv4,TCP
# ip地址+端口号(port)--连接确定的网络进程
dest_arr = ('10.207.39.89', 2000)
# 客户端开始建立连接
chat_client.connect(dest_arr)

epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 标准输入监测
epoll.register(chat_client.fileno(), select.EPOLLIN)  # 接收缓冲区监测

while True:
    events = epoll.poll(-1, 2)
    for fd, event in events:
        if fd == sys.stdin.fileno():  # 代表标准输入里边有数据
            data = input('请输入数据:')
            chat_client.send(data.encode('utf8'))
        elif fd == chat_client.fileno():  # 代表接收缓冲池内有数据
            recv_data = chat_client.recv(100)
            if not recv_data:
                print('对方断开了!')
                exit()
            print(recv_data.decode('utf8'))
