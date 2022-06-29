# @Author : 杨佳杰
# @Time   : 2022/6/14 14:20
# @File   : 3-创建游戏窗口+游戏循环.py
import pygame
import time
pygame.init()
# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))
while True:
    time.sleep(1)
pygame.quit()
