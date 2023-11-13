import pygame

pygame.init()

FPS = 60

# Цвета огня, снарядов и танков игрока и противника
USER_COLOR = (0, 130, 0)
ENEMY_COLOR = (100, 100, 100)
EXPLOSION_COLOR = (255, 0, 0)
BULLET_COLOR = (255, 255, 0)

# Размеры танков
TANK_WIDTH = 60
TANK_HEIGHT = 90
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

X_MIN = TANK_WIDTH//2
X_MAX = WIDTH - TANK_WIDTH
Y_MIN = TANK_HEIGHT//2
Y_MAX = HEIGHT - TANK_WIDTH

path = 'sprites/textures/'
TEXTURES = {
    # '.': pygame.image.load('sprites/textures/backgrounds/background.png'),
    'background': pygame.image.load(path + 'backgrounds/sand.png'),
    'W': pygame.image.load(path + 'objects/stones.png'),
    'G': pygame.image.load(path + 'objects/grass.png'),
    'B': pygame.image.load(path + 'objects/Bricks.png'),
    'O': pygame.image.load(path + 'objects/water.png'),
    # '.': pygame.image.load('sprites/textures/objects/grass.png')
    
    'tank':{
        'body':{
            'user': pygame.image.load(path + 'tanks/user/body1.png'),
            'enemy': pygame.image.load(path + 'tanks/enemy/body.png'),
        },
        'tower':{
            'user': pygame.image.load(path + 'tanks/user/tower1.png'),
            'enemy': pygame.image.load(path + 'tanks/enemy/tower.png'),
        }
    },
    'explosion':{
        1: (pygame.image.load(path + 'explosions/explosion1.png'), 20),
        2: (pygame.image.load(path + 'explosions/explosion2.png'), 70),
        3: (pygame.image.load(path + 'explosions/explosion3.png'), 70),
        4: (pygame.image.load(path + 'explosions/explosion4.png'), 70),
        5: (pygame.image.load(path + 'explosions/explosion5.png'), 60),
        6: (pygame.image.load(path + 'explosions/explosion6.png'), 50),
        7: (pygame.image.load(path + 'explosions/explosion7.png'), 40),
    },

    'scores': pygame.image.load(path + 'gui/points.png')
}

music_path = 'sounds/'
MUSIC = {
    'music': 'sounds/music/main_theme.mp3',
    'effects': {
        'movement': pygame.mixer.Sound(music_path + 'effects/movement.mp3'),
        'shot': pygame.mixer.Sound(music_path + 'effects/shot.mp3'),
        'damage': pygame.mixer.Sound(music_path + 'effects/damage.mp3'),
    }
}