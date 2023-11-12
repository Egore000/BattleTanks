import pygame

FPS = 60

# Цвета огня, снарядов и танков игрока и противника
USER_COLOR = (0, 130, 0)
ENEMY_COLOR = (100, 100, 100)
EXPLOSION_COLOR = (255, 0, 0)
BULLET_COLOR = (255, 255, 0)

# Размеры танков
TANK_WIDTH = 50
TANK_HEIGHT = 70
TOWER_WIDTH = 70
TOWER_HEIGHT = 140

# Размер огня и снарядов
# EXPLOSION_SIZE = 20
BULLET_SIZE = 6

# Скорость движения танка и снаряда. 
velocity = 3
BULLET_SPEED = 40

# Скорость вращения башни
delta = 2

# Параметры окна
WIDTH = 1300
HEIGHT = 630
BACKGROUND_COLOR = (0, 120, 0)

TILE = 30

X_MIN = TANK_WIDTH//2 + TILE
X_MAX = WIDTH - TANK_WIDTH - TILE
Y_MIN = TANK_HEIGHT//2 + TILE
Y_MAX = HEIGHT - TANK_WIDTH - TILE

TEXTURES = {
    # '.': pygame.image.load('sprites/textures/backgrounds/background.png'),
    'background': pygame.image.load('sprites/textures/objects/grass.jpg'),
    'W': pygame.image.load('sprites/textures/objects/stones.png'),
    'G': pygame.image.load('sprites/textures/objects/grass.png'),
    'B': pygame.image.load('sprites/textures/objects/Bricks.png'),
    'O': pygame.image.load('sprites/textures/objects/water.png'),
    # '.': pygame.image.load('sprites/textures/objects/grass.png')
    
    'tank':{
        'body':{
            'user': pygame.image.load('sprites/textures/tanks/user/body1.png'),
            'enemy': pygame.image.load('sprites/textures/tanks/enemy/body.png'),
        },
        'tower':{
            'user': pygame.image.load('sprites/textures/tanks/user/tower1.png'),
            'enemy': pygame.image.load('sprites/textures/tanks/enemy/tower.png'),
        }
    },
    'explosion':{
        1: (pygame.image.load('sprites/textures/explosions/explosion1.png'), 20),
        2: (pygame.image.load('sprites/textures/explosions/explosion2.png'), 70),
        3: (pygame.image.load('sprites/textures/explosions/explosion3.png'), 70),
        4: (pygame.image.load('sprites/textures/explosions/explosion4.png'), 70),
        5: (pygame.image.load('sprites/textures/explosions/explosion5.png'), 60),
        6: (pygame.image.load('sprites/textures/explosions/explosion6.png'), 50),
        7: (pygame.image.load('sprites/textures/explosions/explosion7.png'), 40),
    }
}
