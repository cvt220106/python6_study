# @Author : 杨佳杰
# @Time   : 2022/6/16 10:01
# @File   : 1-tcp客户端.py
from socket import *

tcp_client=socket(AF_INET,SOCK_STREAM)#ipv4,TCP
#ip地址+端口号(port)--连接确定的网络进程
dest_arr=('10.207.39.89',2000)
#客户端开始建立连接
tcp_client.connect(dest_arr)
#连接建立,开始传输 传输的是字节流!!!要加b
tcp_client.send(b'python6 dayday up')
tcp_client.send(b'second send message')
#接受数据
data=tcp_client.recv(100)#字节流!
print(data)
tcp_client.close()