import sys

import pygame
import numpy as np
import time

import settings
from mapmodule import damaged_objects


class Screen:
    '''
    Класс, содержащий настройки
    окна
    '''
    WIDTH = settings.WIDTH
    HEIGHT = settings.HEIGHT
    COLOR = settings.BACKGROUND_COLOR
    X_MIN = settings.X_MIN
    X_MAX = settings.X_MAX
    Y_MIN = settings.Y_MIN
    Y_MAX = settings.Y_MAX


class Explosion:
    # SIZE = settings.EXPLOSION_SIZE

    textures = [
        settings.TEXTURES['explosion'][1],
        # settings.TEXTURES['explosion'][2],
        settings.TEXTURES['explosion'][3],
        # settings.TEXTURES['explosion'][4],
        # settings.TEXTURES['explosion'][5],
        # settings.TEXTURES['explosion'][6],
        # settings.TEXTURES['explosion'][7],
    ]

    def __init__(self, x, y, type_):
        self.x = x
        self.y = y

        self.color = settings.EXPLOSION_COLOR
        self.texture = Explosion.textures
        self.type = type_
    
    # @property
    def pos(self, num):
        return (self.x - self.texture[num][1]//2, self.y - self.texture[num][1]//2)

    def draw(self, screen):
        if self.type == "shot":
            texture = self.texture[0]
            texture = pygame.transform.scale(texture[0], (texture[1], texture[1]))
            screen.blit(texture, self.pos(0))
        else:
            for num, texture in enumerate(self.textures):
                texture = pygame.transform.scale(texture[0], (texture[1], texture[1]))
                texture.set_colorkey((255, 255, 255))
                screen.blit(texture, self.pos(num))


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

    def collideEnemy(self, enemy):
        return self.sprite.colliderect(enemy.body_rect)


    def collideMap(self, damaged_objects):
        idx = self.sprite.collidelist(damaged_objects)
        if idx == -1:
            return False
        return True
        

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
        return Bullet(x, y, player.angle), Explosion(x, y, 'shot')

    def move(player, dx, dy):
        '''
        Метод движения танка. 
        dx и dy принимают значения (-1, 0, 1)
        '''
        if dx < 0:
            x = player.x - settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                player.x = x
            player.body = type(player).body_left
        elif dx > 0:
            x = player.x + settings.velocity
            if Screen.X_MIN <= x <= Screen.X_MAX:
                player.x = x
            player.body = type(player).body_rigth
        
        if dy < 0:
            y = player.y - settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                player.y = y
            player.body = type(player).body
        elif dy > 0:
            y = player.y + settings.velocity
            if Screen.Y_MIN <= y <= Screen.Y_MAX:
                player.y = y
            player.body = type(player).body_flip

        player.body_rect = player.body.get_rect(center=player.pos)

        player.tower_rect = player.tower.get_rect(center=player.pos)
        player.tower.set_colorkey((255, 255, 255))            


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
        self.damage = 50
        
        self.tower = Enemy.tower
        self.tower_rect = self.tower.get_rect(center=self.pos)
        
        self.body = Enemy.body
        self.body_rect = self.body.get_rect(center=self.pos)

    @property
    def pos(self):
        return (self.x, self.y)

    def get_damage(self, user):
        self.hp -= user.damage
        user.exp += 30


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
        self.damage = 40
        self.exp = 0
        
        self.tower = User.tower
        self.tower_rect = self.tower.get_rect(center=self.pos)

        self.body = User.body
        self.body_rect = self.body.get_rect(center=self.pos)
    
    @property
    def pos(self):
        return (self.x, self.y)


class Painter:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, user, enemy, bullets, explosions, world_map):
        for x, y, char in world_map:
            item = settings.TEXTURES[char]
            item = pygame.transform.scale(item, (settings.TILE, settings.TILE))
            self.screen.blit(item, (x, y))
        
        for bullet in bullets:
            sin_a = np.sin(bullet.angle)
            cos_a = np.cos(bullet.angle)
            if (Screen.X_MIN <= bullet.x <= Screen.X_MAX) and \
                    (Screen.Y_MIN <= bullet.y <= Screen.Y_MAX): 
                
                bullet.x += bullet.speed * sin_a
                bullet.y -= bullet.speed * cos_a
                bullet.draw(self.screen)

            else:
                bullets.remove(bullet)
            
            if bullet.collideEnemy(enemy):
                enemy.get_damage(user)

                explosion = Explosion(bullet.x, bullet.y, 'explose')
                explosions.append(explosion)
                bullets.remove(bullet)

            elif bullet.collideMap(damaged_objects):
                explosion = Explosion(bullet.x, bullet.y, 'explose')
                explosions.append(explosion)
                bullets.remove(bullet)

        enemy.draw(self.screen)
        user.draw(self.screen)

        for explosion in explosions:
            explosion.draw(self.screen)
        
        time.sleep(1/settings.FPS)


        for explosion in explosions:
            explosions.remove(explosion)     

if __name__ == "__main__":
    pass