# @Author : 杨佳杰
# @Time   : 2022/6/9 10:55
# @File   : test.py
import wd_message

wd_message.send_message.send()

txt=wd_message.receive_message.receive()
print(txt)