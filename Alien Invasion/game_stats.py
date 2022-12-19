import json

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active = False
        
        # High score should never be reset.
        self.high_score = self.get_high_score()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        # Display the level
        self.level = 1
    
    def get_high_score(self):
        """Retrieve highscore saved from highscore.json"""
        filename = 'Alien Invasion/Data/highscore.json'
        try:
            with open(filename) as f:
                highscore = json.load(f)
        except FileNotFoundError:
            return 0
        else:
            return highscore
        
    def set_high_score(self):
        """Store new highscore in highscore.json"""
        try:
            filename = 'Alien Invasion/Data/highscore.json'
            with open(filename, 'w') as f:
                json.dump(self.high_score, f)
        except FileNotFoundError:
            return 0
        else:
            print(f'Your favorite number {self.high_score} has been stored in {filename.split("/")[2]}')