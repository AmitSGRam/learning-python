import sys

import pygame

from rocket import Rocket
from settings import Settings
from bullet import Bullet

class Rocket_Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and created game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption('Rocket Game')
        
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # Set rocket to an attribute.
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

    def rungame(self):
        """Start the main loop of the game."""
        while True:
            self._checkevents()
            
            self.rocket.updaterocket()
            self.bullets.update()

            self._updatedisplay()

    def _checkevents(self):
        """Check for keyboard and mouse inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
                self._keydownevents(event)
            elif event.type == pygame.KEYUP:
                self._keyupevents(event)

    def _keydownevents(self, event):
        """Respond to keypresses"""

        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _keyupevents(self, event):
        """Respond to key releases."""

        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _updatedisplay(self):
        """Update images on the screen and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    """Make a game instance and run."""

    RG = Rocket_Game()
    RG.rungame()