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


class Explosion:
    SIZE = settings.EXPLOSION_SIZE

    textures = [
        settings.TEXTURES['explosion'][1]
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = settings.EXPLOSION_SIZE
        self.color = settings.EXPLOSION_COLOR
        self.texture = Explosion.textures

    @property
    def pos(self):
        return (self.x - self.size//2, self.y - self.size//2)

    def draw(self, screen):
        for texture in self.textures:
            texture = pygame.transform.scale(texture, (self.size, self.size))
            texture.set_colorkey((255, 255, 255))
            # texture
            screen.blit(texture, self.pos)


class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

        self.speed = settings.BULLET_SPEED
        self.color = settings.BULLET_COLOR
        self.size = settings.BULLET_SIZE
        self.sprite = pygame.Rect(x - self.size//2, y - self.size//2, self.size, self.size)

    def draw(self, screen):
        self.sprite = pygame.Rect(self.x - self.size//2, self.y - self.size//2, self.size, self.size)
        pygame.draw.rect(screen, self.color, self.sprite)



class Tank:
    WIDTH = settings.TANK_WIDTH
    HEIGHT = settings.TANK_HEIGHT
    TOWER_WIDTH = settings.TOWER_WIDTH
    TOWER_HEIGHT = settings.TOWER_HEIGHT
    
    tower = settings.TEXTURES['tank']['tower']
    body = settings.TEXTURES['tank']['body']


    def rotate(player, theta):
        theta *= np.pi/180
        player.angle += theta
        player.angle -= round(player.angle/(2*np.pi)) * 2*np.pi

        player.tower = pygame.transform.rotate(type(player).tower, -player.angle*180/np.pi)
       
        player.tower_rect = player.tower.get_rect(center=player.pos)
        player.tower.set_colorkey((255, 255, 255))

        return player


    def draw(player, screen):
                 
        screen.blit(player.body, player.body_rect)
        screen.blit(player.tower, player.tower_rect)
        
    def shoot(player):
        x = player.x + Tank.TOWER_HEIGHT//2 * np.sin(player.angle)
        y = player.y - Tank.TOWER_HEIGHT//2 * np.cos(player.angle)
        return Bullet(x, y, player.angle), Explosion(x, y)



class Enemy(Tank):
    tower = pygame.transform.scale(Tank.tower['enemy'], (Tank.TOWER_WIDTH, Tank.TOWER_HEIGHT))
    tower.set_colorkey((255, 255, 255))

    body = pygame.transform.scale(Tank.body['enemy'], (Tank.WIDTH, Tank.HEIGHT))
    body.set_colorkey((255, 255, 255))

    body_left = pygame.transform.rotate(body, 90)
    body_left.set_colorkey((255, 255, 255))
    
    body_rigth = pygame.transform.rotate(body, -90)
    body_rigth.set_colorkey((255, 255, 255))
    
    body_flip = pygame.transform.rotate(body, 180)
    body_flip.set_colorkey((255, 255, 255))

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y

        self.angle = angle * np.pi/180
        self.hp = 100
        self.damage = 30
        
        self.tower = Enemy.tower
        self.tower_rect = self.tower.get_rect(center=self.pos)
        
        self.body = Enemy.body
        self.body_rect = self.body.get_rect(center=self.pos)

    @property
    def pos(self):
        return (self.x, self.y)



class User(Tank):
    tower = pygame.transform.scale(Tank.tower['user'], (Tank.TOWER_WIDTH, Tank.TOWER_HEIGHT))
    tower.set_colorkey((255, 255, 255))

    body = pygame.transform.scale(Tank.body['user'], (Tank.WIDTH, Tank.HEIGHT))
    body.set_colorkey((255, 255, 255))

    body_left = pygame.transform.rotate(body, 90)
    body_left.set_colorkey((255, 255, 255))
    
    body_rigth = pygame.transform.rotate(body, -90)
    body_rigth.set_colorkey((255, 255, 255))
    
    body_flip = pygame.transform.rotate(body, 180)
    body_flip.set_colorkey((255, 255, 255))

    def __init__(self, x, y, angle):
        self.x = x 
        self.y = y

        self.angle = angle * np.pi/180
        self.hp = 100
        self.exp = 0
        
        self.tower = User.tower
        self.tower_rect = self.tower.get_rect(center=self.pos)

        self.body = User.body
        self.body_rect = self.body.get_rect(center=self.pos)
    
    @property
    def pos(self):
        return (self.x, self.y)

    def move(self, keys):
        if keys[pygame.K_w]:
            y = self.y - settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                self.y = y

            self.body = User.body
            self.body_rect = self.body.get_rect(center=self.pos)

            self.tower_rect = self.tower.get_rect(center=self.pos)
            self.tower.set_colorkey((255, 255, 255))

        elif keys[pygame.K_s]:
    
            y = self.y + settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                self.y = y

            self.body = User.body_flip
            self.body_rect = self.body.get_rect(center=self.pos)
            
            self.tower_rect = self.tower.get_rect(center=self.pos)
            self.tower.set_colorkey((255, 255, 255))

        elif keys[pygame.K_a]:
            x = self.x - settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                self.x = x
            
            self.body = User.body_left
            self.body_rect = self.body.get_rect(center=self.pos)

            self.tower_rect = self.tower.get_rect(center=self.pos)
            self.tower.set_colorkey((255, 255, 255))
            
        elif keys[pygame.K_d]:
            x = self.x + settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                self.x = x

            self.body = User.body_rigth
            self.body_rect = self.body.get_rect(center=self.pos)

            self.tower_rect = self.tower.get_rect(center=self.pos)
            self.tower.set_colorkey((255, 255, 255))

        return self 


class Painter:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, user, enemy, bullets, explosions, world_map):
        for x, y, char in world_map:
            # pygame.draw.rect(self.screen, settings.TEXTURES.get(char), (x, y, settings.TILE, settings.TILE))
            item = settings.TEXTURES[char]
            item = pygame.transform.scale(item, (settings.TILE, settings.TILE))
            self.screen.blit(item, (x, y))
        
        for bullet in bullets:
            if Screen.X_MIN <= bullet.x <= Screen.X_MAX and \
                Screen.Y_MIN <= bullet.y <= Screen.Y_MAX: 
                bullet.x += bullet.speed * np.sin(bullet.angle)
                bullet.y -= bullet.speed * np.cos(bullet.angle)
                bullet.draw(self.screen)
            else:
                bullets.remove(bullet)

        for explosion in explosions:
            explosion.draw(self.screen)
        
        time.sleep(0.01)

        for explosion in explosions:
            explosions.remove(explosion)     

        enemy.draw(self.screen)
        user.draw(self.screen)

if __name__ == "__main__":
    pass