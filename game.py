# nuh uh

import pygame
from settings import Settings
from player import Player
import game_functions as gf


def run_game():
    pygame.init()
    gm_settings = Settings()
    
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    player = Player(screen)
    
    while True:
        gf.check_events(player)
        player.update()
        gf.update_screen(gm_settings, screen, player)
    
run_game()