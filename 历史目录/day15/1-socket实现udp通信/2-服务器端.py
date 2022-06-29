# @Author : 杨佳杰
# @Time   : 2022/6/15 10:32
# @File   : 2-服务区端.py
from socket import *
import sys
#创建套接字
server=socket(AF_INET,SOCK_DGRAM)#IPV4,UDP

#绑定本地的相关信息,若不绑定,则由系统随机分配
local_addr=(sys.argv[1],2000)#利用系统传参,这样linux方便
server.bind(local_addr)#服务器连接地址开始监听

for i in range(1,4):
    #等待客户端发送信息
    recv_data=server.recvfrom(1024)#1024表示每次最大接受字节


    #显示接收内容
    print(recv_data[0].decode('utf8'))#接受的字节流数据
    print(recv_data[1])#发送数据客户端的ip地址与端口

    #服务器给客户端发送信息
    str1='world'*i
    server.sendto(str1.encode('utf8'),recv_data[1])

#关闭服务器
server.close()
