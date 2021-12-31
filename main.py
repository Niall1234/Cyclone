import pygame
from pygame.locals import *
from pygame.sprite import Group
from cyclone_game_settings import Settings
from event_functions import *
from ring import Ring
from catchzone import CatchZone
from menu import Menu

game_settings = Settings()

clock = pygame.time.Clock()

surface = pygame.display.set_mode((game_settings.width, game_settings.height))
game_ring = Ring(surface)
game_catch_zone = CatchZone(surface, game_settings, game_ring)

game_menu = Menu(game_settings, surface)

pygame.init()

game_font = pygame.font.Font(game_settings.font, 16)

pygame.display.set_caption("Cyclone")

lights = Group()

while True:
    generate_menu(game_font, game_menu, game_settings, clock)
    run_game(surface, game_settings, clock, lights, game_ring, game_catch_zone)
