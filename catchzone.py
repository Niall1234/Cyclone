import pygame

class CatchZone:
    def __init__(self, surface, game_settings, ring):
        self.surface = surface
        self.game_settings = game_settings
        self.ring = ring
        self.width = 20
        self.rect = pygame.Rect(0, 0, self.width, self.width)
        self.rect.center = (self.ring.x_center, self.ring.y_center + self.ring.radius)

