import pygame
import sys
import random
import math
from setting import Setting
from game_start import GameStart
from block import Block
from copy import deepcopy

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

    def _move_map(self, event):
        """移动方块"""
        global step, score, high_score

        # 深拷贝当前地图以比较移动后是否有变化
        original_map = deepcopy(gameMap)
        moved = False
        merged_score = 0  # 本次移动的合并得分

        # 根据移动方向选择遍历顺序和方向
        if event == pygame.K_UP or event == pygame.K_DOWN:
            # 垂直方向（上下）移动
            for j in range(len(gameMap[0])):  # 遍历每一列
                column = [gameMap[i][j] for i in range(len(gameMap))]  # 取出整列

                # 根据方向处理列
                if event == pygame.K_UP:
                    new_column, merged = self._slide_and_merge(column)
                else:  # 向下
                    new_column, merged = self._slide_and_merge(column[::-1])
                    new_column = new_column[::-1]  # 反转回来

                # 更新列并标记移动
                if column != new_column:
                    moved = True
                    for i in range(len(gameMap)):
                        gameMap[i][j] = new_column[i]
                    merged_score += merged

        elif event == pygame.K_LEFT or event == pygame.K_RIGHT:
            # 水平方向（左右）移动
            for i in range(len(gameMap)):  # 遍历每一行
                row = gameMap[i][:]  # 复制整行

                # 根据方向处理行
                if event == pygame.K_LEFT:
                    new_row, merged = self._slide_and_merge(row)
                else:  # 向右
                    new_row, merged = self._slide_and_merge(row[::-1])
                    new_row = new_row[::-1]  # 反转回来

                # 更新行并标记移动
                if row != new_row:
                    moved = True
                    gameMap[i] = new_row
                    merged_score += merged

        # 如果有移动且方块合并了
        if moved:
            step += 1
            score += merged_score  # 增加分数
            if score > high_score:
                high_score = score
            self._new_block()

    def _slide_and_merge(self, tiles):
        """滑动并合并一维数组中的方块"""
        # 1. 删除空格子（0）
        slides = [t for t in tiles if t != 0]

        # 2. 合并相邻的相同方块
        merged = 0  # 本次合并得分
        slides2 = []
        i = 0
        while i < len(slides):
            # 检查是否有两个相同的相邻方块可以合并
            if i + 1 < len(slides) and slides[i] == slides[i + 1]:
                slides2.append(slides[i] * 2)
                merged += slides[i] * 2  # 记录得分
                i += 2  # 跳过下一个元素（因为合并了）
            else:
                slides2.append(slides[i])
                i += 1

        # 3. 在末尾补充0（空格）
        slides2.extend([0] * (len(tiles) - len(slides2)))

        return slides2, merged
    
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
