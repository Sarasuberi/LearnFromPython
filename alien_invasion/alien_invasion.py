import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""

        pygame.init()
        self.settings = Settings()

        # 初始化游戏窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # 全屏模式
        # self.settings.screen_width = self.screen.get_rect().width  # 获取屏幕宽度
        # self.settings.screen_height = self.screen.get_rect().height  # 获取屏幕高度
        pygame.display.set_caption("外星人入侵")

        # 初始化飞船
        self.ship = Ship(self)
        # 初始化子弹组
        self.bullets = pygame.sprite.Group()
        # 初始化外星人组
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self._check_events()  # 监听键盘和鼠标事件
            self.ship.update()  # 更新飞船位置
            self._update_bullet()  # 更新子弹
            self._create_fleet()  # 创建外星人
            self._update_screen()  # 然后每次循环时都会重绘屏幕

    def _check_events(self):
        """响应按键和鼠标事件"""
        """
        每当用户按键时，都将在Pygame中注册一个事件。
        事件都是通过方法pygame.event.get() 获取的，因此需要在方法_check_events() 中指定要检查哪些类型的事件。
        每次按键都被注册为一个KEYDOWN 事件。Pygame检测到KEYDOWN 事件时，需要检查按下的是否是触发行动的键。
        例如，如果玩家按下的是右箭头键，就增大飞船的rect.centerx 值，将飞船向右移动。
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)  # 按下按键事件
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  # 松开按键事件

    """
    随着游戏开发的深入，_check_events() 方法将变得越来越复杂。
    为了让这个方法更易于管理，重构了两个方法分别处理按下和松开按键事件。
    """

    def _check_keydown_events(self, event):
        # 按下按键事件
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # 按下右箭头键，向右的标识符修改成True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # 按下左箭头键，向左的标识符修改成True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()  # 按下空格键，发射子弹
        elif event.key == pygame.K_ESCAPE:
            sys.exit()  # 按下Esc键，退出游戏

    def _check_keyup_events(self, event):
        # 松开按键事件
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self.ship.space = False

    def _create_fleet(self):
        """创建外星人，并且加入Group"""
        """重写创建外星人方法，创建一行外星人"""
        # 计算一行能创建多少外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 计算屏幕可容纳多少行外星人
        Ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (
            3 * alien_height) - Ship_height
        num_rows = available_space_y // (2 * alien_height)

        # 创建外星人群
        for num_row in range(num_rows):
            for num in range(number_aliens_x):
                self._create_alien(num, num_row)

    def _create_alien(self, num: int, num_row: int):
        """重构创建一行外星人的逻辑"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * num
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * num_row
        self.aliens.add(alien)

    def _fire_bullet(self):
        """创建子弹，并且加入Group"""
        """重写了子弹组，为了满足子弹上限的条件"""

        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """把逻辑写成一个方法直接调用"""

        self.bullets.update()  # 更新子弹位置

        # 删除屏幕外的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""

        self.screen.fill(
            self.settings.bg_color)  # 方法fill() 用self.bg_color背景色填充屏幕
        self.ship.blitme()  # 绘制飞船
        # 绘制外星人
        self.aliens.draw(self.screen)
        # for alien in self.alien.sprites():
        #    alien.draw_bullet()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()  # 让最近绘制的屏幕可见

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
