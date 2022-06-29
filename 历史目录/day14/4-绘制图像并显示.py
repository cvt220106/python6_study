# @Author : 杨佳杰
# @Time   : 2022/6/14 14:28
# @File   : 4-绘制图像并显示.py
import pygame
pygame.init()
#创建游戏窗口
screen=pygame.display.set_mode((480,700))
# 绘制背景图像
# 1> 加载图像
bg = pygame.image.load("./images/background.png")
# 2> 绘制在屏幕
screen.blit(bg, (0, 0))
# 绘制英雄图像
# 1> 加载图像
hero = pygame.image.load("./images/me1.png")
# 2> 绘制在屏幕
screen.blit(hero, (200, 500))
#后加载的图像图层在先加载的图像之上
# 3> 更新显示 - update 方法会把之前所有绘制的结果，一次性更新到屏幕窗口上
pygame.display.update()
pygame.quit()
