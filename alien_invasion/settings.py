class Settings:
    """储存一些游戏中的设置的类"""

    # 初始化游戏的设置
    def __init__(self):
        # 屏幕尺寸设置
        self.screen_width = 1200
        self.screen_height = 800

        # 窗体背景色设置
        self.bg_color = (230, 230, 230)

        # 游戏速度控制
        self.game_speed = 1.5

        # 飞船设置
        self.ship_speed = self.game_speed

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = self.game_speed
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 1
        self.fleet_drop_speed = self.alien_speed * 10
        # fleet_direction为1表示向右移，为-1表示向左移。
        self.fleet_direction = 1
