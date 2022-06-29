# @Author : 杨佳杰
# @Time   : 2022/6/16 10:09
# @File   : 2-tcp服务器端.py
from socket import *

tcp_server=socket(AF_INET,SOCK_STREAM)#ipv4,TCP
#ip地址+端口号(port)--连接确定的网络进程
server_arr=('10.207.39.89',2000)
#服务器端与IP地址以及端口建立连接
tcp_server.bind(server_arr)
#开始倾听客户端的连接请求
tcp_server.listen(10)#int值为tcp服务器缓冲区大小!

#如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server就可以省下来专门等待其他新客户端的链接
client_socket, client_addr = tcp_server.accept()

#接受客户端数据
#一次数据多次接收
# recv_data=client_socket.recv(5)
# print(recv_data)
# recv_data=client_socket.recv(15)
# print(recv_data)
#多次数据一次接收
recv_data=client_socket.recv(50)
print(recv_data)
client_socket.send(b'study')
client_socket.close()
tcp_server.close()