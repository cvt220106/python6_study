# @Author : 杨佳杰
# @Time   : 2022/6/14 11:39
# @File   : 2-理解游戏内坐标系.py
import pygame
pygame.init()

hero_rect=pygame.Rect(100,500,120,125)#x,y,width,height

print(f'英雄的原点{hero_rect.x},{hero_rect.y}')
print(f'英雄的尺寸{hero_rect.width},{hero_rect.height}')
print(f'英雄尺寸{hero_rect.size}')