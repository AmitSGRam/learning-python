import pygame

import sys
import random

from Settings import Settings
from Star import Star

class Stars_Game:
    """A class to represent the game."""
    
    def __init__(self):
        """ Initialize the game attributes. """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Stars_Game')
        self.screen_width, self.screen_height = self.screen.get_size()
        self.settings.screen_width,self.settings.screen_height = self.screen_width, self.screen_height
        
        self.stars = pygame.sprite.Group()
        
        self._create_stars()
        
    def run_game(self):
        """Run the game."""
        while True:
            self._check_events()
            
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()
    
    def _keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        
        self.stars.draw(self.screen)
        pygame.display.flip()
    
    def _create_stars(self):
        new_star = Star(self)
        
        star_width, star_height = new_star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_of_stars_x = available_space_x // (2 * star_width)
        
        available_space_y = self.settings.screen_height - (2 * star_height)
        number_of_stars_y = available_space_y // (2 * star_height)
        
        for number_of_star_y in range(number_of_stars_x):
            for number_of_star_x in range(number_of_stars_x):
                self._create_each_star(number_of_star_x, number_of_star_y)
    
    def _create_each_star(self, number_of_star_x, number_of_star_y):
        new_star = Star(self)
        star_width, star_height = new_star.rect.size
        
        new_star.rect.x = star_width + (2 * star_width * number_of_star_x)
        new_star.rect.y = star_height + (2 * star_height * number_of_star_y)
        
        new_star.rect.x += random.randint(-10, 10)
        new_star.rect.y += random.randint(-10, 10)
        
        self.stars.add(new_star)
        
if __name__ == '__main__':
    game = Stars_Game()
    game.run_game()