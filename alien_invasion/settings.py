class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height= 700
        self.bg_color = (0,0,0)

        #Ship Setting
        self.ship_speed_factor = 1.5

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (234,0,195)
        self.bullets_allowed = 3