import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """创建一个外星人类"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人都设置在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的精确水平位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动外星人"""
        self.x += (self.settings.alien_speed * 
                   self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人遇到屏幕左右边缘就返回True"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True