# @Author : 杨佳杰
# @Time   : 2022/6/7 23:03
# @File   : work9-单例模式.py
"""
单例设计模式的目的
让类创建的对象，在系统中只有唯一的一个实例
每一次执行类名()返回的对象，内存地址是相同的
"""


class MusicPlayer:
    # 类属性记录类是否被引用，若引用，则不可继续创建，从而实现单例
    state = None

    def __new__(cls, *args, **kwargs):  # 重写__new__方法
        if cls.state is None:  # 为空则可创建
            cls.state = super().__new__(cls)  # super调用父类的new得到实例对象内存地址
            return cls.state
        # 反之则不创建，返回当前的单例引用
        return cls.state

    def __init__(self, music_name):
        self.music_name = music_name

    def play(self):
        print(f'播放音乐{self.music_name}')


play1=MusicPlayer('love story')
play1.play()
print(play1)
play2=MusicPlayer('青花瓷')
play2.play()
print(play2)
print(play1 is play2)