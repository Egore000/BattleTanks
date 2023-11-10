import settings
import pygame
import sys

class Screen:
    WIDTH = settings.WIDTH
    HEIGHT = settings.HEIGHT
    COLOR = settings.BACKGROUND_COLOR


class Tank:
    WIDTH = settings.TANK_WIDTH
    HEIGHT = settings.TANK_HEIGHT
    GUN_WIDTH = settings.GUN_WIDTH
    GUN_LENGHT = settings.GUN_LENGHT
    TOWER_WIDTH = settings.TOWER_WIDTH
    # def __init__(self, player):
    #     self.color = type(player).COLOR
    #     self.gun_color = (self.color[0]-10, self.color[0]-10, self.color[0]-10)
    #     self.body = pygame.Rect(player.x - Tank.WIDTH // 2, player.y - Tank.HEIGHT // 2, Tank.WIDTH, Tank.HEIGHT)
    #     self.gun = pygame.Rect(player.x - 3, player.y - Tank.HEIGHT // 2 - 40, 6, 60)
    #     self.tower = pygame.()

        # self.model = [
        #     (pygame.Rect(player.x - Tank.WIDTH // 2, player.y - Tank.HEIGHT // 2, Tank.WIDTH, Tank.HEIGHT), self.color),
        #     (pygame.Rect(player.x - 3, player.y - Tank.HEIGHT // 2 - 40, 6, 60), gun_color),
        #     (pygame.circle())
        # ]

    def draw(player, screen):
        color = type(player).COLOR
        r = color[0] - 40 if color[0] > 40 else color[0]
        g = color[1] - 40 if color[1] > 40 else color[1]
        b = color[2] - 40 if color[2] > 40 else color[2]

        gun_color = (r, g, b)

        body = pygame.Rect(player.x - Tank.WIDTH // 2,
                        player.y - Tank.HEIGHT // 2,
                        Tank.WIDTH, 
                        Tank.HEIGHT)
        gun = pygame.Rect(player.x - Tank.GUN_WIDTH // 2,
                        player.y - Tank.HEIGHT // 2 - Tank.GUN_LENGHT/1.5,
                        Tank.GUN_WIDTH,
                        Tank.GUN_LENGHT)
        tower = pygame.Rect(player.x - Tank.WIDTH // 2 + 5,
                        player.y - Tank.HEIGHT // 2 + 10,
                        Tank.TOWER_WIDTH,        
                        Tank.TOWER_WIDTH,)        

        pygame.draw.rect(screen, color, body)
        pygame.draw.rect(screen, gun_color, gun)
        pygame.draw.circle(screen,
                        gun_color,
                        (player.x, player.y),
                        Tank.TOWER_WIDTH//2)

class Enemy:
    COLOR = settings.ENEMY_COLOR
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.angle = angle
        self.hp = 100
        self.damage = 30

    def draw(self, screen):
        Tank.draw(self, screen)

class User:
    COLOR = settings.USER_COLOR
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.angle = angle
        self.color = User.COLOR
        self.hp = 100
        self.exp = 0

    def move(self, key):
        if key == pygame.K_w:
            self.y -= settings.velocity
        elif key == pygame.K_s:
            self.y += settings.velocity
        elif key == pygame.K_a:
            self.x 

    def draw(self, screen):
        Tank.draw(self, screen)

if __name__ == "__main__":
    user = User(200, 200)
    enemy = Enemy(100, 100)
    
    pygame.init()

    screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

        screen.fill(Screen.COLOR)
        # for elem in tank.model:
        #     pygame.draw.rect(screen, elem[1], elem[0])
        enemy.draw(screen)
        user.draw(screen)

        pygame.display.flip()