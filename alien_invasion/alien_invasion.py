import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
import time
from button import Button
from scoreboard import Scoreboard


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

        # 创建一个用于存储游戏统计信息的实例,并且初始化记分板
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        # 初始化飞船
        self.ship = Ship(self)

        # 初始化子弹组
        self.bullets = pygame.sprite.Group()

        # 初始化外星人组
        self.aliens = pygame.sprite.Group()

        # 初始化外星人
        self._create_fleet()

        # 创建开始按钮
        self.play_button = Button(self, "Start")

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self._check_events()  # 监听键盘和鼠标事件
            if self.stats.game_active:
                self.ship.update()  # 更新飞船位置
                self._update_bullet()  # 更新子弹
                self._update_aliens()  #更新外星人位置
                self._fire_bullet()  # 默认射出子弹

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    """
    随着游戏开发的深入，_check_events() 方法将变得越来越复杂。
    为了让这个方法更易于管理，重构了两个方法分别处理按下和松开按键事件。
    """

    def _check_keydown_events(self, event):
        """按下按键事件"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # 按下右箭头键，向右的标识符修改成True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # 按下左箭头键，向左的标识符修改成True
        elif event.key == pygame.K_SPACE:
            # self._fire_bullet()  # 按下空格键，发射子弹
            pass
        elif event.key == pygame.K_RETURN:
            # self.stats.game_active = True
            pass
        elif event.key == pygame.K_ESCAPE:
            sys.exit()  # 按下Esc键，退出游戏

    def _check_keyup_events(self, event):
        """ 松开按键事件"""

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
        #alien_width , alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * num
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * num_row
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        更新外星人群中所有外星人的位置
        并且将检测外星人的位置
        """
        # self._create_fleet()  # 创建外星人

        # 外星人的边缘检测
        self._check_fleet_edges()
        self.aliens.update()

        # 外星人和飞船的碰撞检测
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检测是否有外星人到达了底部
        self._check_aliens_bottom()

        # 移除超过下屏幕的外星人
        # screen_rect = self.screen.get_rect()
        # for alien in self.aliens.copy():
        #    if alien.rect.top <= 0:
        #        self.aliens.remove(alien)

    def _check_fleet_edges(self):
        """外星人的边缘检测"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break

    def _check_fleet_direction(self):
        """将外星人下移，并改变他们的方向"""

        # 切换左右移动
        self.settings.fleet_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        ### 以下内容测试使用，请注释
        # print(self.settings.fleet_direction)
        # print(self.settings.game_speed)

    def _check_aliens_bottom(self):
        """检测外星人是否到达了屏幕低端"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()  # 跟飞船被撞到一样判定失败
                break

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """子弹和外星人的碰撞检测"""

        # 检测子弹和外星人的碰撞
        # 为了测试方便暂时修改成子弹不会消失
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                False, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        # 生成新的外星人
        if not self.aliens:
            self.bullets.empty()  # 如果所有外星人都被击杀了，就删除所有子弹，刷新外星人
            self._create_fleet()
            self.settings.initialize_speedup()

            # 提高等级
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ship_left > 1:

            # 先将ship_left - 1
            self.stats.ship_left -= 1
            self.scoreboard.prep_ships()

            self._clear_game()
            """
            # 然后清空所有外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建新的外星人，并将飞船重新放到游戏初始位置
            self._create_fleet()
            self.ship.center_ship()
            
            """

            # 暂停
            time.sleep(1)
        else:
            self.stats.game_active = False

            # 显示鼠标光标
            pygame.mouse.set_visible(True)

    def _check_play_button(self, mouse_pos):
        """鼠标按键位置检测"""

        # 按下开始按钮时开始新的游戏
        button_clicker = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicker and not self.stats.game_active:

            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)

            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()
            self._clear_game()

    def _clear_game(self):

        # 然后清空所有外星人和子弹
        self.aliens.empty()
        self.bullets.empty()

        # 重置游戏速度设置
        self.settings.initialize_dynamic_settings()

        # 创建新的外星人，并将飞船重新放到游戏初始位置
        self._create_fleet()
        self.ship.center_ship()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""

        # 方法fill() 用self.bg_color背景色填充屏幕
        self.screen.fill(self.settings.bg_color)

        # 绘制记分板
        self.scoreboard.show_score()

        # 绘制飞船
        self.ship.blitme()

        # 绘制外星人
        self.aliens.draw(self.screen)

        # 如果游戏处于非活跃状态，就绘制开始按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':

    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
