import pygame, sys
from settings import *
from level import Level


pygame.init()



screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Fight back the Darkness!')
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    screen.fill('black')
    level.run()
    # draw all our elements
    # update everything
    pygame.display.update()
    # nothing in this loop should run over 60 frames
    clock.tick(60)


