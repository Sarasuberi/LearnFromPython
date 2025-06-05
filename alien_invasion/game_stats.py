class GameStats:
    """跟踪游戏的统计信息类"""

    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0
        self.high_score = 0

        # 设置游戏启动标识符
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1