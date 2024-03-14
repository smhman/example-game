# nuh uh

import pygame
pygame.init()

#ekraan smh
screen = pygame.display.set_mode([800, 500])

running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        pygame.display.flip()

pygame.quit() 
