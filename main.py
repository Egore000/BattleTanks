import pygame
import sys
from tools import *
from mapmodule import world_map
from settings import *

pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
f = pygame.font.SysFont('arial', 30)
paint = Painter(screen)
clock = pygame.time.Clock()
pygame.display.update()
background = TEXTURES['background'].convert()

user = User(200, 200, 0)
enemy = Enemy(500, 200, 117)

run = True
bullets = []
explosions = []
# print(world_map)
while run:
    screen.fill(settings.BACKGROUND_COLOR)
    # screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet, explosion = user.shoot()
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
    elif keys[pygame.K_a]:
        user.move(-1, 0)
    elif keys[pygame.K_s]:
        user.move(0, 1)
    elif keys[pygame.K_d]:
        user.move(1, 0)

    paint.draw(user, enemy, bullets, explosions, world_map)

    if enemy.hp <= 0:
        del enemy
        x = np.random.randint(Screen.X_MIN, Screen.X_MAX)
        y = np.random.randint(Screen.Y_MIN, Screen.Y_MAX)
        enemy = Enemy(x, y, 30)

    print(user.exp)
    # screen_text = f.render(str(user.exp), 1, (255, 0, 0))
    pygame.display.flip()