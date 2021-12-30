import pygame
from pygame.locals import *
from pygame.sprite import Group
from cyclone_game_settings import Settings
from event_functions import *
from ring import Ring
from catchzone import CatchZone

game_settings = Settings()

clock = pygame.time.Clock()

surface = pygame.display.set_mode((game_settings.width, game_settings.height))
game_ring = Ring(surface)
game_catch_zone = CatchZone(surface, game_settings, game_ring)


pygame.init()
pygame.display.set_caption("Cyclone")

lights = Group()

while True:
    run_game(surface, game_settings, clock, lights, game_ring, game_catch_zone)
