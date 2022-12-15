import pygame

import sys

from Settings import Settings
from Raindrop import Raindrop

from random import randint

class Raindrops:
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Raindrops')
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen.get_size()
        
        self.raindrops = pygame.sprite.Group()
        self._create_raindrop()
        
    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_display()
    
    def _update_display(self):
        
        self.screen.fill(self.settings.bg_color)
        
        self.raindrops.draw(self.screen)
        
        pygame.display.flip()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def _create_raindrop(self):
        new_raindrop = Raindrop(self)
        #self.raindrops.add(new_raindrop)
        raindrop_width, raindrop_height = new_raindrop.rect.size
        
        available_row_x = self.screen_width - (2 * raindrop_width)
        number_x = available_row_x // (2 * raindrop_width)
        
        available_row_y = self.screen_height - (2 * raindrop_height)
        number_y = available_row_y // (2 * raindrop_height)
        
        for rain_y in range(number_y):
            for rain_x in range(number_x):
                self._create_raindrops(rain_x, rain_y)
                
    def _create_raindrops(self,rain_x, rain_y):
        new_raindrop = Raindrop(self)
        raindrop_width, raindrop_height = new_raindrop.rect.size
        new_raindrop.rect.x = raindrop_width + (2*raindrop_width*rain_x)
        
        new_raindrop.y = raindrop_height * 2* rain_y
        new_raindrop.rect.y = new_raindrop.y
        
        new_raindrop.rect.x += randint(-10,10)
        new_raindrop.rect.y += randint(-10,10)
        
        self.raindrops.add(new_raindrop)
        
    def _update_raindrops(self):
        #for ra in self.raindrops:
            #ra.rect.y += self.settings.raindrop_fallspeed
        self.raindrops.update()
        create_new_raindrops = False
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top>self.screen_rect.bottom:
                raindrop.remove()
                create_new_raindrops = True
    
if __name__ == '__main__':
    raindrops = Raindrops()
    raindrops.run_game()