import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """显示得分信息的类"""

    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # 准备初始得分图像
        self.prep_score()

        # 准备最高的分图像
        self.prep_high_score()

        # 初始化等级
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""

        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,
                                            self.text_color,self.settings.bg_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 80

    def prep_high_score(self):
        """将最高的分转换为渲染的图像"""

        high_score = round(self.stats.high_score,-1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,
                                                 self.text_color,self.settings.bg_color)

        # 将最高分放在屏幕的中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        # self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = self.screen_rect.top

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        """
            创建一个空的编组，用于存储飞船实例
            为了填充这个编组，根据玩家还有多少搜飞船以相应的次数运行一个循环
            在这个循环中，创建新飞船并设置x坐标，让整个飞船组都位于屏幕的左侧差10像素
            还将y坐标设置为离屏幕上边缘10像素，让所有飞船都出现在屏幕的左上角
            最后将所有飞船都添加进编组ships中
        """
        self.ships = Group()
        for num_ship in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + num_ship * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):

        # 显示得分
        self.screen.blit(self.score_image,self.score_rect)

        # 显示最高分
        self.screen.blit(self.high_score_image,self.high_score_rect)

        # 显示等级
        self.screen.blit(self.level_image,self.level_rect)

        # 显示剩余飞船
        self.ships.draw(self.screen)

    def check_high_score(self):
        """检查是否产生了新的最高分"""

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """将等级转换为渲染的图像"""

        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,
                                            self.text_color,self.settings.bg_color)

        # 将等级放在屏幕中央
        self.level_rect = self.level_image.get_rect()
        self.level_rect.center = self.screen_rect.center
        self.level_rect.top = self.score_rect.top
