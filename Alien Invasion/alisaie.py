import pygame

class Alisaie:
    """A class to manage the game character."""

    def __init__(self, ai_game):
        """Initialize the image and set its position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get its rect.
        self.image = pygame.image.load('Alien Invasion/images/Alisaie.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the image at its current location."""
        self.screen.blit(self.image, self.rect)