class Settings:
    """ 
    储存一些游戏中的设置的类
    初始化游戏的设置
    """
    def __init__(self,ai_game):

        self.scoreboard = ai_game.scoreboard
        # 屏幕尺寸设置
        self.screen_width = 1200
        self.screen_height = 800

        # 窗体背景色设置
        self.bg_color = (230, 230, 230)

        # 游戏速度控制
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

    def initialize_dynamic_settings(self):
        """初始化游戏速度变化设置"""

        self.game_speed = 1

        # 飞船速度设置
        self.ship_speed = self.game_speed

        # 子弹速度设置
        self.bullet_speed = self.game_speed

        # 外星人速度设置
        self.alien_speed = (self.game_speed / 2)
        self.fleet_drop_speed = (self.alien_speed * 10)

        # fleet_direction为1表示向右移，为-1表示向左移。
        self.fleet_direction = (self.game_speed / 2)

        # 记分用
        self.alien_points = 10

    def initialize_speedup(self):

        # 加速咯
        self.game_speed *= self.speedup_scale
        self.ship_speed = self.game_speed
        self.bullet_speed = self.game_speed
        self.alien_speed = (self.game_speed / 2)
        self.fleet_drop_speed = (self.alien_speed * 10)
        self.alien_points = int(self.alien_points * self.score_scale)