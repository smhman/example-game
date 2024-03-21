# nuh uh

import pygame
from settings import Settings

pygame.init()
gm_settings = Settings()

screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
pygame.display.set_caption(gm_settings.caption)


running = True
while running:
    screen.fill(gm_settings.bg_color)    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False

    pygame.display.flip()

pygame.quit() 

