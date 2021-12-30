import pygame
from pygame.sprite import Sprite


class Light(Sprite):
    def __init__(self, surface, center_pos, game_settings):
        super(Light, self).__init__()
        self.surface = surface
        self.center_pos = center_pos
        self.game_settings = game_settings
        self.radius = 10
        self.border_width = 2
        self.border_colour = (255, 255, 255)

    def draw_light(self):
        pygame.draw.circle(self.surface, self.border_colour, self.center_pos, self.radius, self.border_width)


