import pygame
import sys
import random
import math
from setting import Setting
from game_start import GameStart
from block import Block

# 游戏地图。[宽 X 高]
gameMap = [[0 for _ in range(4)] for _ in range(4)]
SIDE = 90   # 常量: 方块边长(像素)
step = 0  # 有效操作步数。如果按键后没有方块移动就不算有效操作
score = 0
high_score = 0

class TwoBlock:
    """创建游戏资源和行为"""

    def __init__(self) -> None:
        """初始化游戏和创建游戏资源"""

        # 初始化设置
        pygame.init()
        self.settings = Setting()

        # 初始化游戏窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("2048")

        # 创建一个新的游戏
        self.start = GameStart(self)
        self.bolck = Block(self)

        # 创建初始方块
        self._make_map()

    def running(self):
        """开始游戏的主循环"""

        while True:
            self._check_events()  # 监听键盘和鼠标事件
            if self.start.game_active:
                pass
            self._update_screen()  # 然后每次循环时都会重绘屏幕

    def _check_events(self):
        """响应按键和鼠标事件"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)  # 按下按键事件

    def _check_keydown_events(self, event):
        """按下按键事件"""

        if event.key == pygame.K_RIGHT:
            self._move_map(pygame.K_RIGHT)
        elif event.key == pygame.K_LEFT:
            self._move_map(pygame.K_LEFT)
        elif event.key == pygame.K_UP:
            self._move_map(pygame.K_UP)
        elif event.key == pygame.K_DOWN:
            self._move_map(pygame.K_DOWN)
        elif event.key == pygame.K_ESCAPE:
            sys.exit()  # 按下Esc键，退出游戏

    def _move_map(self,event):
        """移动方块"""

        global step, score,high_score

        # 检查本次按键是否移动了方块，移动则生成新方块
        hasMoved = False
        for process in range(len(gameMap[0]) -1):
            for i in range(len(gameMap)):
                for j in range(len(gameMap[0])):
                    if gameMap[i][j] == 0:
                        continue

                    # 按下上键，上移
                    if event == pygame.K_UP and i != 0 and gameMap[i][j] == gameMap[i - 1][j]:
                        gameMap[i - 1][j] *= 2 # 上面的块的数值乘2
                        score += gameMap[i - 1][j]
                        gameMap[i][j] = 0
                        hasMoved = True
                    if event == pygame.K_UP and i != 0 and gameMap[i - 1][j] == 0: # 上方的块是0，则上移但不合并
                        gameMap[i - 1][j] = gameMap[i][j]
                        gameMap[i][j] = 0
                        hasMoved = True

                    # 按下下键，下移
                    if event == pygame.K_DOWN and i != len(gameMap) - 1 and gameMap[i][j] == gameMap[i + 1][j]:
                        gameMap[i + 1][j] *= 2
                        score += gameMap[i + 1][j]
                        gameMap[i][j] = 0
                        hasMoved = True
                    if event == pygame.K_DOWN and i != len(gameMap) - 1 and gameMap[i + 1][j] == 0:
                        gameMap[i + 1][j] = gameMap[i][j]
                        gameMap[i][j] = 0
                        hasMoved = True

                    # 按下左键，左移
                    if event == pygame.K_LEFT and j != 0 and gameMap[i][j] == gameMap[i][j - 1]:
                        gameMap[i][j - 1] *= 2
                        score += gameMap[i][j - 1]
                        gameMap[i][j] = 0
                        hasMoved = True
                    if event == pygame.K_LEFT and j != 0 and gameMap[i][j - 1] == 0:
                        gameMap[i][j - 1] = gameMap[i][j]
                        gameMap[i][j] = 0
                        hasMoved = True

                    # 按下右键，右移
                    if event == pygame.K_RIGHT and j != len(gameMap[0]) - 1 and gameMap[i][j] == gameMap[i][j + 1]:
                        gameMap[i][j + 1] *= 2
                        score += gameMap[i][j + 1]
                        gameMap[i][j] = 0
                        hasMoved = True
                    if event == pygame.K_RIGHT and j != len(gameMap[0]) - 1 and gameMap[i][j + 1] == 0:
                        gameMap[i][j + 1] = gameMap[i][j]
                        gameMap[i][j] = 0
                        hasMoved = True

        if hasMoved:
            global step
            step += 1
            self._new_block()

    def _draw_bg(self):
        """画一个方块移动背景"""

        # 方块间距
        spacing = 10

        # 绘制gameMap
        for i in range(len(gameMap)):
            for j in range(len(gameMap[0])):
                leftPos = j * (SIDE + spacing) + 10  # 方块左侧位置
                topPos = i * (SIDE + spacing) + 10  # 方块顶部位置
                if gameMap[i][j] == 0:
                    pygame.draw.rect(self.screen, (205, 193, 180), (leftPos, topPos, SIDE, SIDE), border_radius=8)
                else:
                    # 绘制矩形
                    pygame.draw.rect(self.screen, (self.bolck.getBlockColor(gameMap[i][j])), (leftPos, topPos, SIDE, SIDE), border_radius=8)

                    # 显示方块对应的数字。字号根据文字宽度自适应。
                    font_block = pygame.font.SysFont("Microsoft YaHei", math.floor(70 - len(str(gameMap[i][j])) * 8), True)

                    # 字体颜色：浅色方块用黑色，深色方块用白色
                    if gameMap[i][j] == 2 or gameMap[i][j] == 4:
                        fontColor = (124, 115, 106)
                    else:
                        fontColor = (249, 246, 242)

                    # 设置文字
                    text_blockNum = font_block.render(str(gameMap[i][j]), True, fontColor)

                    # 计算出字符与居中的偏移，也就是该移动多少像素就能使文字居中
                    centerOffset_lateral = SIDE / 2 - text_blockNum.get_width() / 2  # 水平
                    centerOffset_vertical = SIDE / 2 - text_blockNum.get_height() / 2  # 垂直

                    # 显示文字
                    self.screen.blit(text_blockNum, (leftPos + centerOffset_lateral, topPos + centerOffset_vertical))
        textsBase = (SIDE + spacing) * len(gameMap)

        # 显示游戏数据
        font_yahei = pygame.font.SysFont("Microsoft YaHei", 20)
        text_score_info = font_yahei.render("分数：" + str(score) + "  步数：" + str(step),
                                      True, (0, 0, 0))
        text_high_score_info = font_yahei.render("最高分：" + str(high_score),
                                                 True, (0, 0, 0))
        self.screen.blit(text_score_info,
                         (10, textsBase + 20))  # 根据计算，显示在游戏区域下方
        self.screen.blit(text_high_score_info,(250, textsBase + 20))

        # 显示提示或版权文字
        text_tips = font_yahei.render("按上下左右即可移动数字", True, (0, 0, 0))
        self.screen.blit(text_tips, (10, textsBase + 50))

        # 判断是否输了游戏，是则显示Game Over文字
        if self._referee() == 2:
            self.start.game_active = False
            font_lostGame = pygame.font.SysFont("Microsoft YaHei", 40, True)    # 字体设置
            text_lostGame = font_lostGame.render("Game Over!", True, (255, 255, 255), (0, 0, 0))    # 输出文字
            text_lostGame_PosX = self.screen.get_width() / 2 - text_lostGame.get_width() / 2
            text_lostGame_PosY = self.screen.get_height() / 2 - text_lostGame.get_height() / 2
            self.screen.blit(text_lostGame, (text_lostGame_PosX, text_lostGame_PosY))   # 在界面上打印

    def _referee(self) -> int:
        movable = False
        for i in range(len(gameMap)):  # 遍历每一行
            for j in range(len(gameMap[0])):  # 遍历每一行的每一个方块
                if i != 0 and gameMap[i - 1][j] == gameMap[i][j]:
                    movable = True  # 该方块上方是否有同类(可移动，游戏可以进行)
                if i != len(gameMap) - 1 and gameMap[i + 1][j] == gameMap[i][j]:
                    movable = True  # 该方块下方是否有同类
                if j != 0 and gameMap[i][j - 1] == gameMap[i][j]:
                    movable = True  # 该方块左方是否有同类
                if j != len(gameMap[0]) - 1 and gameMap[i][j + 1] == gameMap[i][j]:
                    movable = True  # 该方块右方是否有同类
                if gameMap[i][j] == 0:
                    movable = True
                if gameMap[i][j] == 2048:
                    return 1    # 赢了
        if movable is True:
            return 0    # 继续
        else:
            return 2    # 输了

    def _getRandoPos(self) -> list:
        """随机生成一个数字方块的位置（位置保证在gameMap内）"""

        # 收集所有空位置
        empty_positions = []
        for i in range(len(gameMap)):
            for j in range(len(gameMap[0])):
                if gameMap[i][j] == 0:
                    empty_positions.append((i, j))

        # 如果有空位，随机选择一个返回
        if empty_positions:
            return random.choice(empty_positions)
        else:
            # 没有空位时返回None（后续需要处理这种情况）
            return None

    def _make_map(self)-> None:
        """生成初始方块"""

        block1 = self._getRandoPos()
        blokc2 = self._getRandoPos()
        if random.randint(0, 10) == 0:
            gameMap[block1[0]][block1[1]] = 4
        else:
            gameMap[block1[0]][block1[1]] = 2
        gameMap[blokc2[0]][blokc2[1]] = 2

    def _new_block(self) -> None:
        """在随机位置生成一个新方块"""

        # 获取随机位置
        block = self._getRandoPos()
        if block is not None:
            # 如果有空位，随机生成2或4
            if random.randint(0, 10) == 0:
                gameMap[block[0]][block[1]] = 4
            else:
                gameMap[block[0]][block[1]] = 2
            

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""

        # 方法fill() 用self.bg_color背景色填充屏幕
        self.screen.fill(self.settings.bg_color)

        # 初始化游戏背景方块
        self._draw_bg()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == "__main__":
    TwoBlock().running()
