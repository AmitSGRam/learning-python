class Settings:
    """A class to store settings of the project."""

    def __init__(self):
        """Initialize project settings."""

        self.bg_color = (230,230,230)

        # Set the resolution of game.
        self.screen_width = 1200
        self.screen_height = 900
        # Set speed of the rocket.
        self.rocket_speed = 5
        self.rocket_limit = 2
        
        # Alien Settings
        self.alien_speed = 0.000001
        
        # Bullet Settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 200
        self.bullet_color = (100, 60, 60)
        self.bullets_allowed = 15