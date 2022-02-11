import json

class GameStats:
    """Tracks statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initializes statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in  inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """Gets the high score if it exist"""
        try:
            with open('highscore.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0 

    def reset_stats(self):
        """Initializes statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
