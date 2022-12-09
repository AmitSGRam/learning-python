import pygame

from settings import Settings 

class Rocket:
    """A class to represent Rocket to be used in Rocket Game."""

    def __init__(self, rg):
        """Initialize the rocket and its position."""

        self.screen = rg.screen
        self.screen_rect = self.screen.get_rect()

        # Load the settings to an attribute.
        self.settings = Settings()
        
        # Load the rocket image and get its rect.
        self.image = pygame.image.load('Rocket_Game/rocket.bmp')
        self.image_rect = self.image.get_rect()

        # Set initial position of the rocket.
        self.image_rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def updaterocket(self):
        """Update rocket's position based on the Movement flag."""

        # Update ship's x.
        if self.moving_right and self.image_rect.right<self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.image_rect.left>0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.image_rect.top>0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.image_rect.bottom<self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        
        # Update ship's x to rect.
        self.image_rect.x = self.x
        self.image_rect.y = self.y

    def blitme(self):
        """Load rocket image to game."""

        self.screen.blit(self.image, self.image_rect)