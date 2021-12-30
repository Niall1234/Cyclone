import pygame, sys
from pygame.locals import *
from pygame.sprite import Sprite, Group
from light import Light

def run_game(surface, game_settings, clock, lights, ring, catchzone):
    surface.fill(game_settings.bg_color)
    get_ring(lights, ring, surface, game_settings)
    check_events(game_settings, catchzone, ring)
    pygame.display.update()
    clock.tick(game_settings.fps)
    check_light_count(game_settings, ring)





def check_events(game_settings, catchzone, ring):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not game_settings.space_pressed:
                    game_settings.space_pressed = True
            check_for_win(game_settings, catchzone, ring)
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                game_settings.space_pressed = False



def get_ring(lights, ring, surface, game_settings):
    for i in range(len(ring.x_positions)):
        new_light = Light(surface, (ring.x_positions[i], ring.y_positions[i]), game_settings)
        lights.add(new_light)

    ring.draw_ring(lights)
    ring.blinking_light(game_settings.light_count)

def check_light_count(game_settings, ring):
    if game_settings.light_count > len(ring.x_positions):
        game_settings.light_count = 0

    game_settings.light_count += 1

def check_for_win(game_settings, catchzone, ring):
    if game_settings.space_pressed and catchzone.rect.collidepoint(ring.blinking_light_rect.center):
        print("you win")
    else:
        print("you lose")
