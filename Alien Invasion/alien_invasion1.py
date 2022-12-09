import sys

import pygame

from settings import Settings
from ship import Ship
from alisaie import Alisaie
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Set game character to an attribute.
        self.alisaie = Alisaie(self)

        # Set Ship to an attribute.
        self.ship = Ship(self)
        # Set Bullet to an attribute.
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right.
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        # Move the ship to the left.
                        self.ship.moving_left = True
                    elif event.key == pygame.K_SPACE:
                        # Fire the bullets.
                        if len(self.bullets) < self.settings.bullets_allowed:
                            new_bullet = Bullet(self)
                            self.bullets.add(new_bullet)
                    elif event.key == pygame.K_q:
                        # Exit the game
                        sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right.
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        # Move the ship to the left.
                        self.ship.moving_left = False
            
            self.ship.update()
            # Update bullet positions.
            self.bullets.update()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            # Redraw the screen during each pass through the loop.
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            # Draw the game character to game.
            self.alisaie.blitme()
            # Draw the ship to game.
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()