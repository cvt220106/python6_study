# @Author : 杨佳杰
# @Time   : 2022/6/17 15:01
# @File   : 1-服务器端.py
from socket import *
import os
import struct
#创建服务端 套接字
server_socket=socket(AF_INET,SOCK_STREAM)
local_addr=('10.207.39.89',2000)
#服务器端绑定ip与端口
server_socket.bind(local_addr)
server_socket.listen(10)
#连接成功
client_socket,addr=server_socket.accept()
print(addr)
#发文件名
file_name='README'
#先发报文头--文件名的长度
b_file_name=file_name.encode('utf8')
client_socket.send(struct.pack("I",len(b_file_name)))
#发送文件名
client_socket.send(b_file_name)

#再发文件内容长度
file=open(file_name,'rb')
text_b=file.read()
client_socket.send(struct.pack("I",len(text_b)))
#发送文件内容
client_socket.send(text_b)
file.close()
client_socket.close()
server_socket.close()
