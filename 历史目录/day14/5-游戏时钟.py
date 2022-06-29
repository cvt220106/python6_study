# @Author : 杨佳杰
# @Time   : 2022/6/14 14:39
# @File   : 5-游戏时钟.py
import pygame

# 创建游戏时钟对
clock=pygame.time.Clock()
i=0
#游戏循环
while True:
    # 设置屏幕刷新帧率，每秒 60 次
    clock.tick(60)

    print(i)
    i+=1