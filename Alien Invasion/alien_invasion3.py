import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_SPACE:
                        if len(self.bullets) < self.settings.bullets_allowed:
                            new_bullet = Bullet(self)
                            self.bullets.add(new_bullet)
                    elif event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

            self.ship.update()
            self.bullets.update()
            
            self.screen.fill(self.settings.bg_color)

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.ship.blitme()

            pygame.display.flip()
            

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()