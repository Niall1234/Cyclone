class Menu:
    def __init__(self, game_settings, surface):
        self.game_settings = game_settings
        self.surface = surface
        self.colour = (255, 155, 0)
        self.menu_in_progress = True

    def get_surface(self):
        self.surface.fill(self.colour)

    def generate_text(self, font):
        font_surf = font.render("Press ANY KEY to play", True, (255, 255, 255))
        font_rect = font_surf.get_rect()
        font_rect.center = (int(self.game_settings.width / 2), int(self.game_settings.height / 2))
        self.surface.blit(font_surf, font_rect)

