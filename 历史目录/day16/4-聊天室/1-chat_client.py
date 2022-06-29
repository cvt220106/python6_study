# @Author : 杨佳杰
# @Time   : 2022/6/16 10:01
# @File   : 1-tcp客户端.py
from socket import *
import select
import sys

chat_client = socket(AF_INET, SOCK_STREAM)  # ipv4,TCP
if len(sys.argv)<2:
    print(':chat ip input!')
    exit(0)
# ip地址+端口号(port)--连接确定的网络进程
dest_arr = (sys.argv[1], 2000)
# 客户端开始建立连接
chat_client.connect(dest_arr)
name=input('请输入自己的姓名:')

epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 标准输入监测
epoll.register(chat_client.fileno(), select.EPOLLIN)  # 接收缓冲区监测

while True:
    events = epoll.poll(-1, 2)
    for fd, event in events:
        if fd == sys.stdin.fileno():  # 代表标准输入里边有数据
            try:
                data = input()
            except:
                print('I will go!')
                chat_client.close()
                exit(2)
            message=name+':'+data
            chat_client.send(message.encode('utf8'))
        elif fd == chat_client.fileno():  # 代表接收缓冲池内有数据
            recv_data = chat_client.recv(100)
            if not recv_data:
                exit(1)
            print(recv_data.decode('utf8'))
