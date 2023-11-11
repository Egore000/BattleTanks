# Цвета огня, снарядов и танков игрока и противника
USER_COLOR = (0, 130, 0)
ENEMY_COLOR = (100, 100, 100)
EXPLOSION_COLOR = (255, 0, 0)
BULLET_COLOR = (255, 255, 0)

# Размеры танков
TANK_WIDTH = 40
TANK_HEIGHT = 60
GUN_WIDTH = TANK_WIDTH // 7
GUN_LENGHT = 1.2 * TANK_HEIGHT
TOWER_WIDTH = 30

# Размер огня и снарядов
EXPLOSION_SIZE = 12
BULLET_SIZE = 6


# Скорость движения танка и снаряда. 
velocity = 3
BULLET_SPEED = 40

# Скорость вращения башни
delta = 2

# Параметры окна
WIDTH = 1300
HEIGHT = 630
BACKGROUND_COLOR = (0, 0, 0)
X_MIN = TANK_WIDTH//2
X_MAX = WIDTH - TANK_WIDTH
Y_MIN = TANK_HEIGHT//2
Y_MAX = HEIGHT - TANK_WIDTH

TILE = 30
TEXTURES = {
    'W': (30, 30, 10),
    'B': (134, 11, 17),
    'G': (20, 141, 3),
}
