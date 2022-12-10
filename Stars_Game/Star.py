import pygame

from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent the stars."""
    
    def __init__(self, stars_game):
        """Initialize a star."""
        super().__init__()
        self.screen = stars_game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('Stars_Game/Images/star.png')
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = self.rect.width, self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)