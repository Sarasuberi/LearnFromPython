import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        
        # 初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.seetings = ai_game.settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        '''
        调用pygame.image.load() 加载图像，并将飞船图像的位置传递给它。
        该函数返回一个表示飞船的surface，而我们将这个surface赋给了self.image 。
        加载图像后，使用get_rect() 获取相应surface的属性rect ，以便后面能够使用它来指定飞船的位置
        
        处理rect 对象时，可使用矩形四角和中心的x坐标和y坐标。可通过设置这些值来指定矩形的位置。
        要让游戏元素居中，可设置相应rect 对象的属性center 、centerx 或centery ；要让游戏元素与屏幕边缘对齐，可使用属性top 、bottom 、left 或right 。
        除此之外，还有一些组合属性，如midbottom 、midtop 、midleft 和midright 。要调整游戏元素的水平或垂直位置，可使用属性x 和y ，分别是相应矩形左上角的x坐标和y坐标。
        这些属性让你无须做游戏开发人员原本需要手工完成的计算，因此会经常用到。
        注意！！
        在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。在1200 x 800的屏幕上，原点位于左上角，而右下角的坐标为(1200,800)。
        这些坐标对应的是游戏窗口，而不是物理屏幕
        '''

        # 将每艘新飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        # 飞船移动标识符
        self.moving_right = False
        self.moving_left = False
        self.space = False

    def update(self):
        """根据移动标识符调整飞船的位置"""
        """根据标识符来确认键盘的操作，然后更新飞船的位置"""
        """目前运行看起来缺少一个边界的设定，飞船会飞出屏幕 = ="""

        # 更新了一个边界检测，防止飞船飞出屏幕,俗称空气墙
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.seetings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.seetings.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = int(self.x)

    def blitme(self):
        
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
