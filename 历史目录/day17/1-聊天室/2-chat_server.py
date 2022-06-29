# @Author : 杨佳杰
# @Time   : 2022/6/16 10:09
# @File   : 2-tcp服务器端.py
from socket import *
import select


chat_server = socket(AF_INET, SOCK_STREAM)  # ipv4,TCP
# ip地址+端口号(port)--连接确定的网络进程
server_arr = ('192.168.0.98', 2000)
# 服务器端与IP地址以及端口建立连接
chat_server.bind(server_arr)
# 开始倾听客户端的连接请求
chat_server.listen(10)  # int值为tcp服务器缓冲区大小!

epoll = select.epoll()
# epoll检测对象
epoll.register(chat_server.fileno(), select.EPOLLIN)

# 存放聊天室内client信息
client_socket_list = []
while True:

    epoll_list = epoll.poll()
    for fd, event in epoll_list:
        if fd == chat_server.fileno():
            # 有客户端连接上
            client_socket, _ = chat_server.accept()  # 获取客户端通信所用的套接字
            # 为该客户注册epoll
            print(f'{client_socket}已连接!')
            client_socket_list.append(client_socket)
            epoll.register(client_socket.fileno(), select.EPOLLIN)
        for client_socket in client_socket_list:
            if fd == client_socket.fileno():
                recv_data = client_socket.recv(1024)
                if not recv_data:
                    epoll.unregister(client_socket.fileno())
                    client_socket_list.remove(client_socket)
                    client_socket.close()
                else:
                    for other_client_socket in client_socket_list:
                        if other_client_socket is not client_socket:
                            other_client_socket.send(recv_data)

client_socket.close()
chat_server.close()
