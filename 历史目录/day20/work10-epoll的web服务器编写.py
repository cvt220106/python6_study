# @Author : 杨佳杰
# @Time   : 2022/6/21 23:47
# @File   : work10-epoll的web服务器编写.py
from socket import *
import re
import select


def service_client(new_socket, request):
    # 接受请求并进行解析
    if not request:
        return
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

    epoll = select.epoll()

    epoll.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = {}

    while True:
        fd_event_list = epoll.poll()
        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():  # 有新的请求连接
                new_socket, client_addr = tcp_server_socket.accept()
                epoll.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            else:
                recv_data = fd_event_dict[fd].recv(4096).decode('utf8')
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epoll.unregister(fd)
                    del fd_event_dict[fd]

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
