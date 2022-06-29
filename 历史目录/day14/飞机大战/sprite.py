# @Author : 杨佳杰
# @Time   : 2022/6/14 20:09
# @File   : sprite.py
import random
import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)  # x,y,width,height
# 屏幕刷新频率
FRAME_PER_SEC = 15

# 定义敌机和子弹的event常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_ENEMY2_EVENT = pygame.USEREVENT + 2
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """整个游戏项目的精灵"""

    def __init__(self, image_name, speed=1):
        # 每个精灵都是一个图像,以及移动的speed
        # 调用pygame精灵父类的初始化
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  # 获取图像的尺寸
        self.speed = speed

    def update(self):
        """通过不断更改图像的坐标达到移动的效果"""
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1调用父类方法实现精灵的创建与属性的定义(image/rect/speed)
        super().__init__("./images/background.png")

        # 2由于是使用两个图像交替出现,实现背景动画效果,第二张的初始化位置坐标需改变
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()  # 调用父类
        # 2,当背景完全移出屏幕时,重新设置会上方,从而达到循环效果
        if self.rect.y == SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1调用父类的方法实现创建
        super().__init__("./images/enemy1.png")
        # 2敌机的移动速度定义为随机1-3
        self.speed = random.randint(1, 3)
        # 3指定敌机的随机出现位置
        self.rect.bottom = 0  # bottom=y+height,相当于快速定义y=-height

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

        # 判断敌机是否飞出屏幕,若飞出,则销毁
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()  # kill方法,将精灵从精灵组移出,销毁精灵


class Enemy2(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1调用父类的方法实现创建
        super().__init__("./images/enemy2.png")
        # 2敌机的移动速度定义为随机1-3
        self.speed = random.randint(1, 3)
        # 3指定敌机的随机出现位置
        self.rect.bottom = 0  # bottom=y+height,相当于快速定义y=-height

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

        # 判断敌机是否飞出屏幕,若飞出,则销毁
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()  # kill方法,将精灵从精灵组移出,销毁精灵


class Hero(GameSprite):
    """"英雄精灵"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)  # 英雄不自动移动
        # 设置英雄的起始位置
        self.yspeed = 0  # 定义飞机上下移动的速度
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        self.rect.y += self.yspeed
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):

        for i in (0, 1, 2):
            for j in (0, 1):
                bullet = Bullet()
                bullet2 = Bullet2()
                # 设置子弹的位置
                bullet.rect.bottom = self.rect.y + i * 20
                bullet.rect.centerx = self.rect.x + j * self.rect.width
                bullet2.rect.bottom = self.rect.y + i * 20
                bullet2.rect.centerx = self.rect.centerx

                # 将子弹添加至精灵组
                self.bullets.add(bullet)
                self.bullets2.add(bullet2)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法,设置初始速度
        super().__init__("./images/bullet1.png", -8)

    def update(self):
        super().update()

        # 判断是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass


class Bullet2(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法,设置初始速度
        super().__init__("./images/bullet2.png", -10)

    def update(self):
        super().update()

        # 判断是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
