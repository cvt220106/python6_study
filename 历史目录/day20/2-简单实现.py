# @Author : 杨佳杰
# @Time   : 2022/6/21 15:32
# @File   : 2-简单实现.py
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
local_addr = ('10.207.53.130', 2000)
server_socket.bind(local_addr)
server_socket.listen(10)

client_socket, client_addr = server_socket.accept()
recv_data = client_socket.recv(1024)
print(recv_data.decode('utf8'))

# #响应 =响应头部+body
http_header = "HTTP/1.1 200 OK\r\n"
response = http_header + '\r\n'
response += 'hello wolrd'
client_socket.send(response.encode('utf8'))
client_socket.close()
server_socket.close()
