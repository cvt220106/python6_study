# @Author : 杨佳杰
# @Time   : 2022/6/17 15:35
# @File   : 2-客户端.py
from socket import *
import struct

client_socket=socket(AF_INET,SOCK_STREAM)

dest_addr=('10.207.39.89',2000)
#请求连接
client_socket.connect(dest_addr)

#先接文件名长度
filename_len=client_socket.recv(4)#指明接收字节长度
#接收文件名
filename=client_socket.recv(struct.unpack("I",filename_len)[0])
print(filename)
#此时文件名为字节流,进行decode
file=open(filename.decode('utf8'),'wb')
#接收文件长度
file_len=client_socket.recv(4)
#接收文件内容
file_content=client_socket.recv(struct.unpack("I",file_len)[0])
file.write(file_content)
file.close()
client_socket.close()