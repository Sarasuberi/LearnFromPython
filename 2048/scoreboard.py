import pygame.font

class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, tb_game):
        self.tb_game = tb_game
        self.screen = tb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tb_game.settings
        self.stats = tb_game.stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()

        # 准备最高的分图像
        self.prep_high_score()

    def prep_score(self):
        """初始化得分图像"""
        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,
                                            self.text_color,self.settings.bg_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left - 20
        self.score_rect.bottom = 80


    def prep_high_score(self):
        """初始化最高分图像"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = 80
