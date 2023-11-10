import pygame
import sys
from tools import *

pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

user = User(200, 200, 0)
enemy = Enemy(100, 100, 0)

pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

run = True
bullets = []
explosions = []
while run:
    current_time = pygame.time.get_ticks()
    screen.fill(Screen.COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet, explosion = user.shoot()
            bullets.append(bullet)
            explosions.append(explosion)
        
    keys = pygame.key.get_pressed()        
    
    for explosion in explosions:
        pygame.draw.rect(screen, settings.EXPLOSION_COLOR, explosion)

    screen.fill(Screen.COLOR)

    user.move(keys)
    if keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_LEFT]:
        Tank.rotate(user, -settings.delta)
    elif keys[pygame.K_RIGHT]:
        Tank.rotate(user, settings.delta)

    for bullet in bullets:

        if Screen.X_MIN <= bullet.x <= Screen.X_MAX and \
            Screen.Y_MIN <= bullet.y <= Screen.Y_MAX: 
            bullet.x += bullet.speed * np.sin(bullet.angle)
            bullet.y -= bullet.speed * np.cos(bullet.angle)
        # bullet.sprite = pygame.Rect(bullet.x, )
            bullet.draw(screen)
        else:
            bullets.remove(bullet)

    enemy.draw(screen)
    user.draw(screen)
    pygame.display.flip()