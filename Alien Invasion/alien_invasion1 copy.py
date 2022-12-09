import sys

import pygame

from settings import Settings
from ship import Ship
from alisaie import Alisaie
from bullet import Bullet
# you'll be able to shoot every 450ms
RELOAD_SPEED = 150

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.firing = True
        self.shot = []
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.reloaded = True
        self.space = pygame.K_SPACE
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
            self._check_events()
            
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            # Redraw the screen during each pass through the loop.
            self._update_screen()  

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            if event.type == pressed[self.space]:
            # when the reload timer runs out, reset it
                self.reloaded = True
                pygame.time.set_timer(pressed[self.space], 0)
            if pressed[pygame.K_SPACE]:
                if len(self.bullets) < self.settings.bullets_allowed:
                    new_bullet = Bullet(self)
                    if self.reloaded:
                        self.bullets.add(new_bullet)
                        print(self.bullets.add(new_bullet))
                        self.reloaded = False
                        pygame.time.set_timer(pressed[self.space], RELOAD_SPEED)
                    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        pressed = pygame.key.get_pressed()
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # Exit the game
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        pass

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
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