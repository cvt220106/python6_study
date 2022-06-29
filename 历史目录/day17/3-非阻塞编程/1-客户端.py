# @Author : 杨佳杰
# @Time   : 2022/6/17 19:51
# @File   : 1-客户端.py
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
dest_addr = ('10.207.39.89', 2000)
client_socket.connect(dest_addr)

client_socket.send(b'hello python')
client_socket.close()
