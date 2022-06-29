# @Author : 杨佳杰
# @Time   : 2022/6/21 23:47
# @File   : work10-多线程web服务器编写.py
from socket import *
import re
from threading import Thread


def service_client(new_socket):
    # 接受请求并进行解析
    request = new_socket.recv(4096).decode('utf8')
    request_lines = request.splitlines()
    print(request_lines)
    if request_lines:
        filename = ''
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])  # 只要第一行!
        if ret:
            filename = ret.group(1)
            if filename == '/':  # 默认请求的即为/
                filename = '/index.html'  # 将请求定位转向另一个页面内容

        try:
            f = open('./day20/http/html' + filename, 'rb')  # 打开本地下对应文件,以字节流形式
        except:  # 没有对应文件返回404
            response = 'HTTP/1.1 404 NOT FOUND\r\n'
            response += '\r\n'
            response += '---------file not found------'
            new_socket.send(response.encode('utf8'))
        else:
            html_content = f.read()  # 字节流
            f.close()
            response = 'HTTP/1.1 200 OK\r\n'
            response += '\r\n'
            new_socket.send(response.encode('utf8'))  # 字符串和字节流分开发送
            new_socket.send(html_content)

    new_socket.close()  # close关闭后自动发送本次传输的字节长度


def main():
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用
    local_addr = ("", 2000)
    tcp_server_socket.bind(local_addr)
    tcp_server_socket.listen(128)

    while True:  # 持续监听,重复连接
        new_socket, client_addr = tcp_server_socket.accept()
        # 创建子进程去进行响应服务,主进程持续循环监听连接
        p = Thread(target=service_client, args=(new_socket,))
        p.start()
        # new_socket.close()  #多线程中此处不可以关闭,因此线程间共享,关闭后会影响已经运行的子线程

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
