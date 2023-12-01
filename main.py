import sys

import pygame

from tools import *
from mapmodule import world_map
from settings import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
score = TEXTURES['scores'].convert()
score = pygame.transform.scale(score, (200, 50))
f = pygame.font.SysFont('arial', 30)
paint = Painter(screen)

global sound
sound = Sounds(MUSIC)
sound.play_music()
movement = sound.movement()

background = TEXTURES['background'].convert()
background = pygame.transform.scale(background, (Screen.WIDTH, Screen.HEIGHT))

user = User(200, 200, 0)
enemy = Enemy(500, 200, 30)

run = True
bullets = []
explosions = []

while run:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet, explosion = user.shoot()
            sound.play_shot()
            bullets.append(bullet)
            explosions.append(explosion)
        
    keys = pygame.key.get_pressed()        
        
    if keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_LEFT]:
        Tank.rotate(user, -settings.delta)
    elif keys[pygame.K_RIGHT]:
        Tank.rotate(user, settings.delta)
    
    if keys[pygame.K_w]:
        user.move(0, -1)
        movement.play()
    elif keys[pygame.K_a]:
        user.move(-1, 0)
        movement.play()
    elif keys[pygame.K_s]:
        user.move(0, 1)
        movement.play()
    elif keys[pygame.K_d]:
        user.move(1, 0)
        movement.play()

    movement.stop()
    # sound.stop_movement()

    paint.draw(user, enemy, bullets, explosions, world_map, sound)
    screen.blit(score, (0, Screen.HEIGHT - 50))
    screen_text = f.render(str(user.exp), 1, (0, 138, 14))
    health_text = f.render(str(user.hp), 1, (240, 10, 13))
    screen.blit(screen_text, (40, Screen.HEIGHT - 45))
    screen.blit(health_text, (130, Screen.HEIGHT - 45))

    if enemy.hp <= 0:
        user.exp += 30
        del enemy
        x = np.random.randint(Screen.X_MIN, Screen.X_MAX)
        y = np.random.randint(Screen.Y_MIN, Screen.Y_MAX)
        alpha = np.random.randint(-45, 45)
        enemy = Enemy(x, y, alpha)
    
    pygame.display.flip()