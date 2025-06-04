import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """创建一个外星人类"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人都设置在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的精确水平位置
        self.x = float(self.rect.x)