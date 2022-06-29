# @Author : 杨佳杰
# @Time   : 2022/6/15 10:27
# @File   : 1-客户端.py
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#ipv4,UDP
#服务器端地址与端口
dest_addr=('10.207.39.89',2000)
for i in range(1,4):
    #发送请求
    str1='hello'*i
    client.sendto(str1.encode('utf8'),dest_addr)
    #接受数据
    recv_data=client.recvfrom(100)#内部参数为要接受的收据大小,windows下可大不可小
    print(recv_data[0].decode('utf8'))
    print(recv_data[1])

client.close()