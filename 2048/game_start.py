class GameStart:
    """游戏开始信息类"""
    
    def __init__(self,tb_game) -> None:
        self.setting = tb_game.settings
        self.reset_start()
        self.score = 0
        self.high_score = 0
        
        # 设置游戏启动标识符
        self.game_active = False
        
    def reset_start(self):
        self.score = 0