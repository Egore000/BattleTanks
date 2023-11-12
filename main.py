import pygame
import sys
from tools import *
from map import world_map
from settings import *

pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
paint = Painter(screen)
clock = pygame.time.Clock()
pygame.display.update()

user = User(200, 200, 0)
enemy = Enemy(500, 200, 117)

run = True
bullets = []
explosions = []
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet, explosion = user.shoot()
            bullets.append(bullet)
            explosions.append(explosion)
        
    keys = pygame.key.get_pressed()        
    
    user.move(keys)
    if keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_LEFT]:
        Tank.rotate(user, -settings.delta)
    elif keys[pygame.K_RIGHT]:
        Tank.rotate(user, settings.delta)

    paint.draw(user, enemy, bullets, explosions, world_map)

    pygame.display.flip()