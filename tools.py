import settings
import pygame
import sys
import numpy as np
import time

class Screen:
    WIDTH = settings.WIDTH
    HEIGHT = settings.HEIGHT
    COLOR = settings.BACKGROUND_COLOR
    X_MIN = settings.X_MIN
    X_MAX = settings.X_MAX
    Y_MIN = settings.Y_MIN
    Y_MAX = settings.Y_MAX



class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

        self.speed = settings.BULLET_SPEED
        self.sprite = pygame.Rect(x-3, y-3, 6, 6)
        self.color = (255, 255, 0)

    def draw(self, screen):
        self.sprite = pygame.Rect(self.x, self.y, 5, 5)
        pygame.draw.rect(screen, self.color, self.sprite)

    def clear(self, screen):
        self.sprite = pygame.Rect(self.x, self.y, 5, 5)
        pygame.draw.rect(screen, Screen.COLOR, self.sprite)



class Tank:
    WIDTH = settings.TANK_WIDTH
    HEIGHT = settings.TANK_HEIGHT
    GUN_WIDTH = settings.GUN_WIDTH
    GUN_LENGHT = settings.GUN_LENGHT
    TOWER_WIDTH = settings.TOWER_WIDTH

    def rotate(player, theta):
        theta *= np.pi/180
        player.angle += theta
        player.angle -= round(player.angle/(2*np.pi)) * 2*np.pi
    
        return player

    def move(player, x, y):
        if keys[pygame.K_w]:
            y = player.y - settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                player.y = y
            player.w = Tank.WIDTH
            player.h = Tank.HEIGHT
            x = player.x - Tank.WIDTH//2
            y = player.y - Tank.HEIGHT//2
            # player.angle = 0
            player.body = pygame.Rect(x, y, player.w, player.h)

        elif keys[pygame.K_s]:
            y = player.y + settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                player.y = y
            player.w = Tank.WIDTH
            player.h = Tank.HEIGHT
            x = player.x - Tank.WIDTH//2
            y = player.y - Tank.HEIGHT//2
            # player.angle = np.pi
            player.body = pygame.Rect(x, y, player.w, player.h)

        elif keys[pygame.K_a]:
            x = player.x - settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                player.x = x
            player.w = Tank.HEIGHT
            player.h = Tank.WIDTH
            x = player.x - Tank.HEIGHT//2
            y = player.y - Tank.WIDTH//2
            # player.angle = -np.pi/2
            player.body = pygame.Rect(x, y, player.w, player.h)
            
        elif keys[pygame.K_d]:
            x = player.x + settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                player.x = x
            player.w = Tank.HEIGHT
            player.h = Tank.WIDTH
            x = player.x - Tank.HEIGHT//2
            y = player.y - Tank.WIDTH//2
            # player.angle = np.pi/2

            player.body = pygame.Rect(x, y, player.w, player.h)
        return player 

    def draw(player, screen):
        color = type(player).COLOR
        r = max(color[0] - 40, 0)
        g = max(color[1] - 40, 0)
        b = max(color[2] - 40, 0)
        
        gun_color = (r, g, b)
        
        start = (player.x, player.y)
        end = (player.x + Tank.GUN_LENGHT * np.sin(player.angle), player.y - Tank.GUN_LENGHT * np.cos(player.angle))
                       
        pygame.draw.rect(screen, color, player.body)
        pygame.draw.line(screen, gun_color, start, end, Tank.GUN_WIDTH) 
        pygame.draw.circle(screen,
                        gun_color,
                        (player.x, player.y),
                        Tank.TOWER_WIDTH//2)

    def shoot(player):
        x = player.x + Tank.GUN_LENGHT * np.sin(player.angle)
        y = player.y - Tank.GUN_LENGHT * np.cos(player.angle)
        explosion = pygame.Rect(x-6, y-6, 12, 12)
        return Bullet(x, y, player.angle), explosion



class Enemy(Tank):
    COLOR = settings.ENEMY_COLOR
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.x0 = x - Tank.WIDTH//2
        self.y0 = y - Tank.HEIGHT//2
        self.w = Tank.WIDTH
        self.h = Tank.HEIGHT

        self.angle = angle * np.pi/180
        self.hp = 100
        self.damage = 30
        
        self.body = pygame.Rect(self.x - Tank.WIDTH//2, self.y - Tank.HEIGHT//2, self.w, self.h)


class User(Tank):
    COLOR = settings.USER_COLOR
    def __init__(self, x, y, angle):
        self.x = x 
        self.y = y
        self.x0 = x - Tank.WIDTH//2
        self.y0 = y - Tank.HEIGHT//2
        self.w = Tank.WIDTH
        self.h = Tank.HEIGHT

        self.angle = angle * np.pi/180
        self.color = User.COLOR
        self.hp = 100
        self.exp = 0
        
        self.body = pygame.Rect(self.x - Tank.WIDTH//2, self.y - Tank.HEIGHT//2, self.w, self.h)

    def move(self, keys):
        if keys[pygame.K_w]:
            y = self.y - settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                self.y = y
            self.w = Tank.WIDTH
            self.h = Tank.HEIGHT
            x = self.x - Tank.WIDTH//2
            y = self.y - Tank.HEIGHT//2
            # player.angle = 0
            self.body = pygame.Rect(x, y, self.w, self.h)

        elif keys[pygame.K_s]:
            y = self.y + settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                self.y = y
            self.w = Tank.WIDTH
            self.h = Tank.HEIGHT
            x = self.x - Tank.WIDTH//2
            y = self.y - Tank.HEIGHT//2
            # player.angle = np.pi
            self.body = pygame.Rect(x, y, self.w, self.h)

        elif keys[pygame.K_a]:
            x = self.x - settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                self.x = x
            self.w = Tank.HEIGHT
            self.h = Tank.WIDTH
            x = self.x - Tank.HEIGHT//2
            y = self.y - Tank.WIDTH//2
            # player.angle = -np.pi/2
            self.body = pygame.Rect(x, y, self.w, self.h)
            
        elif keys[pygame.K_d]:
            x = self.x + settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                self.x = x
            self.w = Tank.HEIGHT
            self.h = Tank.WIDTH
            x = self.x - Tank.HEIGHT//2
            y = self.y - Tank.WIDTH//2
            # player.angle = np.pi/2

            self.body = pygame.Rect(x, y, self.w, self.h)
        return self 


class Painter:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, user, enemy, bullets, world_map):
        for bullet in bullets:
            if Screen.X_MIN <= bullet.x <= Screen.X_MAX and \
                Screen.Y_MIN <= bullet.y <= Screen.Y_MAX: 
                bullet.x += bullet.speed * np.sin(bullet.angle)
                bullet.y -= bullet.speed * np.cos(bullet.angle)
                bullet.draw(self.screen)
            else:
                bullets.remove(bullet)

        enemy.draw(self.screen)
        user.draw(self.screen)

        for x, y, char in world_map:
            pygame.draw.rect(self.screen, settings.TEXTURES.get(char), (x, y, settings.TILE, settings.TILE))

if __name__ == "__main__":
    pass