import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, aigame):

        super().__init__()
        self.settings = aigame.settings
        self.color = self.settings.bullet_color
        self.screen = aigame.screen
        self.ship_rect = aigame.ship.rect

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = self.ship_rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw(self.screen, self.color, self.rect)