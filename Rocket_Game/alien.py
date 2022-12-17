import pygame

from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, rg):
        super().__init__()
        self.screen = rg.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = rg.settings
        
        self.image = pygame.image.load('Rocket_Game/alien.png')
        self.rect = self.image.get_rect()
        #self.rect.x, self.rect.y = self.rect.size
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.left = self.screen_rect.right
        alien_y = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_y)
        alien_x = self.settings.screen_width - self.rect.width
        self.rect.x = randint(0, alien_x)
        
        self.x= float(self.rect.x)
        
    def update(self):
        #self.x -= self.settings.alien_speed
        self.rect.x -= self.settings.alien_speed