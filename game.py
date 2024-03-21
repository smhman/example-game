import pygame
from settings import Settings
from player import Player
from bubble import Bubble
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()

    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    
    clock = pygame.time.Clock()
    
    player = Player(screen)
    
    bubbles = pygame.sprite.Group()

    while True:
        gf.check_events(gm_settings, screen, player, bubbles)
        player.update()
        gf.update_bubbles(player, bubbles)
        bubbles.update()
        gf.update_screen(gm_settings, screen, player, bubbles, clock)

run_game()