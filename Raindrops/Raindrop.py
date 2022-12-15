import pygame

from pygame.sprite import Sprite

class Raindrop(Sprite):
    
    def __init__(self, rdrop):
        super().__init__()
        
        self.screen = rdrop.screen
        #self.screen_rect = rdrop.screen.get_rect()
        self.settings = rdrop.settings
        
        self.image = pygame.image.load('Raindrops/images/raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.rect.width, self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        self.y += self.settings.raindrop_fallspeed
        self.rect.y = self.y