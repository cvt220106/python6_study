# @Author : 杨佳杰
# @Time   : 2022/6/17 19:54
# @File   : 2-服务器非阻塞编程.py
from socket import *


server_socket = socket(AF_INET, SOCK_STREAM)

# 重用对应地址和端口
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

local_addr = ('10.207.39.89', 2000)
server_socket.bind(local_addr)
server_socket.listen(100)

# 非阻塞编程
server_socket.setblocking(False)
client_socket = None

while True:
    try:
        client_socket, client_addr = server_socket.accept()
    except Exception as e:
        pass
    if client_socket:  # 判断是否接收到客户端请求,为None则不做处理,继续循环监听等待
        client_socket.setblocking(False)  # 设置为非阻塞
        try:
            recv_data = client_socket.recv(1000)
            if not recv_data:
                print('连接断开!')
                exit(0)  # 客户端连接断开时,服务器端也断开连接
            print(recv_data.decode('utf8'))
        except Exception as e:
            pass
