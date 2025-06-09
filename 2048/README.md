# 2048
## 项目规划
尝试完成2048这款游戏。
初始化4X4的方块格子并且初始化两个2的数字方块。
游戏开始时，以玩家开始操作方向键为起点开始计时。
创建数字块的类。
玩家可以使用上下左右方向键来操作所有的方块使其往一个方向移动。
当两个方块触碰到一起的时候解析方块内的数字来，如果相同则相加，如果不同就不加。
玩家的任务是把所有数字加到2048 。如果达到了2048就结束游戏弹出“恭喜”字样。
也可以直接消掉2048这个方块游戏继续。
增加记分，如果有方块相加就记分，没有就不记。
首先需要创建一个Pygame的窗口，初始化游戏界面。

## 项目结构
```
alien_invasion/
|-- alien.py
|-- alien_invasion.py
|-- bullet.py
|-- button.py
|-- game_stats.py
|-- settings.py
|-- ship.py
|-- scoreboard.py
|-- sprite.py
|-- README.md
```

## 代码说明
### alien.py
定义了外星人类
### alien_invasion.py
游戏主程序
### bullet.py
定义了子弹类
### button.py
定义了按钮类
### game_stats.py
定义了游戏统计信息类
### settings.py
定义了游戏设置类
### ship.py
定义了飞船类
### scoreboard.py
定义了记分板类
### sprite.py
定义了精灵类
### README.md
项目说明文档
### requirements.txt
项目需要支持的库