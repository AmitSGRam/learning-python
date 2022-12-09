class Settings:
    """A class to store settings of the project."""

    def __init__(self):
        """Initialize project settings."""

        self.bg_color = (230,230,230)

        # Set the resolution of game.
        self.screen_width = 1920
        self.screen_height = 1080
        # Set speed of the rocket.
        self.rocket_speed = 1
        
        # Bullet Settings
        self.bullet_speed = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6