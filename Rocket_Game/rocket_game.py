import sys
from time import sleep

import pygame

from random import randint
from rocket import Rocket
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class Rocket_Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and created game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption('Rocket Game')
        
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # Set rocket to an attribute.
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def rungame(self):
        """Start the main loop of the game."""
        while True:
            self._checkevents()
            
            if self.stats.game_active:
                self.rocket.updaterocket()
                self._update_bullets()
                self._update_aliens()

            # Redraw the screen during each loop of the game.
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
    
    def _update_bullets(self):
        """Update the bullets"""
        self.bullets.update()
        
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()     
        
            
    def _create_fleet(self):
        """Create a fleet of aliens."""
        alien = Alien(self)      
        available_y = self.settings.screen_height - (10 * alien.rect.height)
        number_y = available_y // (2 * alien.rect.height)
        
        available_x = self.settings.screen_width - (4* alien.rect.width) - self.rocket.image_rect.width
        number_x = available_x // (4 * alien.rect.width)
        
        for alien_y in range(number_y):
            for alien_x in range(number_x):
                alien = Alien(self)
                alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_y + self.rocket.image_rect.width
                alien.rect.x = (self.settings.screen_width + 2 * alien.rect.width * alien_x)
                alien.rect.y += randint(-10,10)
                self.aliens.add(alien)

    def _update_aliens(self):
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()
        
        self._check_left()
            
    def _rocket_hit(self):
        """Respond to the rocket being hit by an alien."""
        if self.stats.rockets_left > 0:
            self.stats.rockets_left -= 1
            
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.rocket.center_rocket()
            
            sleep(0.5)
        
        else:
            self.stats.game_active = False
        
    def _check_left(self):
        """Check if any aliens have reached the left of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                # Treat this the same as if the rocket got hit.
                self._rocket_hit()
                break
                        
    def _updatedisplay(self):
        """Update images on the screen and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    """Make a game instance and run."""

    RG = Rocket_Game()
    RG.rungame()