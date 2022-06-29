# @Author : 杨佳杰
# @Time   : 2022/6/17 20:17
# @File   : 3.py
# 作者: 王道 龙哥
# 2022年06月17日10时07分27秒
from socket import *


tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 本地IP地址和端口
address = ('10.207.39.89', 2000)

tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)
#设置tcp_server_socket为非阻塞
tcp_server_socket.setblocking(False)
client_socket = None

while True:
    try:
        client_socket, clientAddr = tcp_server_socket.accept()
    except Exception as e:
        # print(e)
        pass
    if client_socket:
        # 设置client_socket为非阻塞
        client_socket.setblocking(False)
        try:
            text = client_socket.recv(1024)
            # 如果对方断开
            if not text:
                print('byebye')
                exit(0)
            print(text.decode('utf-8'))
        except Exception as e:
            pass