import pygame
import sys
from tools import *

pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

user = User(100, 100)
while True:
    screen.fill(Screen.COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    user.draw(screen)
    pygame.display.flip()