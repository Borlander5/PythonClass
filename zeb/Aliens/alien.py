import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the laien and set its rect attribute."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('C:\\Users\\Kids\\source\\repos\\PythonClass\\zeb\\Aliens\\images\\AlienShip.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.route = 1
        self.routeCount = 0
 
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left"""

        if self.route == 1:
            self.x += (self.settings.alien_speed * self.settings.fleet_direction)
            self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        elif self.route == 2:
            self.x -= (self.settings.alien_speed * self.settings.fleet_direction)
        elif self.route == 3:
            self.y -= (self.settings.alien_speed * self.settings.fleet_direction)
        elif self.route == 4:
             self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        elif self.route == 5:
            self.x -= (self.settings.alien_speed * self.settings.fleet_direction)
            self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        elif self.route >= 6:
            self.y += (self.settings.alien_speed * self.settings.fleet_direction)

        self.routeCount += 1
        if self.routeCount >= 125:
            self.route += 1
            self.routeCount = 0
        self.rect.x = self.x
        self.rect.y = self.y