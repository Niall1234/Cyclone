import pygame

class Ring:
    def __init__(self, surface):
        self.surface = surface
        self.light_colour = (255, 255, 50)
        self.blinking_light_rect = pygame.Rect(0, 0, 12, 12)
        self.width = 600
        self.height = 600
        self.radius = int(self.width / 3)
        self.x_center = int(self.width / 2)
        self.y_center = int(self.height / 2)
        self.x_positions = [
            self.x_center - self.radius,
            self.x_center - self.radius * 0.9,
            self.x_center - self.radius * 0.7,
            self.x_center - self.radius * 0.4,
            self.x_center,
            self.x_center + self.radius * 0.4,
            self.x_center + self.radius * 0.7,
            self.x_center + self.radius * 0.9,
            self.x_center + self.radius,
            self.x_center + self.radius * 0.9,
            self.x_center + self.radius * 0.7,
            self.x_center + self.radius * 0.4,
            self.x_center,
            self.x_center - self.radius * 0.4,
            self.x_center - self.radius * 0.7,
            self.x_center - self.radius * 0.9,
            self.x_center - self.radius
        ]
        self.y_positions = [
            self.y_center,
            self.y_center - self.radius * 0.3,
            self.y_center - self.radius * 0.6,
            self.y_center - self.radius * 0.9,
            self.y_center - self.radius,
            self.y_center - self.radius * 0.9,
            self.y_center - self.radius * 0.6,
            self.y_center - self.radius * 0.3,
            self.y_center,
            self.y_center + self.radius * 0.3,
            self.y_center + self.radius * 0.6,
            self.y_center + self.radius * 0.9,
            self.y_center + self.radius,
            self.y_center + self.radius * 0.9,
            self.y_center + self.radius * 0.6,
            self.y_center + self.radius * 0.3,
            self.y_center
        ]

    def draw_ring(self, lights):
        for light in lights:
            light.draw_light()

    def blinking_light(self, count):
        if count < len(self.x_positions):
            center = (self.x_positions[count], self.y_positions[count])
        else:
            center = (self.x_positions[0], self.y_positions[0])

        pygame.draw.circle(self.surface, self.light_colour, center, 12)
        self.blinking_light_rect.center = center


