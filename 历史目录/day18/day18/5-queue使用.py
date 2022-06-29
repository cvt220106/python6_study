# 作者: 王道 龙哥
# 2022年06月18日10时29分40秒
from multiprocessing import Queue

q = Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())  # False
q.put("消息3")
print(q.full())  # True

# 因为消息列队已满,下面的try都会抛出异常，第一个try会等待2秒后再抛出异常
try:
    q.put("消息4", True, 1)
except Exception as e:
    print("消息列队已满，现有消息数量:%s" % q.qsize())
# 如果队列满，立马抛异常
try:
    q.put_nowait("消息4")
except Exception as e:
    print("消息列队已满，现有消息数量:%s" % q.qsize())

print(q.full())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
print(q.get_nowait())  # 拿的时候没数据，不等，会抛异常
