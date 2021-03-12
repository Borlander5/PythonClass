import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """A class to  represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("/Users/bradleyweldy/pythonclass/shep/Aliens/images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start eaach new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.path = 1
        self.pathCount = 0
        self.yDirection = 1
        self.xDirection = 1
        self.fake_bottom = 300


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.xDirection * self.settings.alien_speed
        self.y += self.yDirection * self.settings.alien_speed
        self.fake_bottom += 0.1
        screen_rect = self.screen.get_rect()
        
        if self.y >= self.fake_bottom or self.y <= 0:
            self.yDirection *= -1
        elif self.x >= screen_rect.right or self.x <= 0:
            self.xDirection *= -1
        
                
        self.rect.x = self.x
        self.rect.y = self.y

"""
    def update(self):
        

        if self.path == 1:
            self.x -= self.settings.alien_speed
            self.y /= self.settings.alien_speed
        elif self.path == 2:
            self.x += self.settings.alien_speed 
            self.y *= self.settings.alien_speed 
        elif self.path == 3:
            self.x += self.settings.alien_speed
            self.y -= self.settings.alien_speed
        elif self.path == 4:
            self.x *= self.settings.alien_speed
            self.y += self.settings.alien_speed           
        elif self.path == 5:
            self.x += self.settings.alien_speed
            self.y /= self.settings.alien_speed
        elif self.path >= 6:
            self.y += self.settings.alien_speed 

        self.pathCount += 2
        if self.pathCount >= 500:
            self.path += 1
            self.pathCount = 0



            
        self.rect.x = self.x
        self.rect.y = self.y    
        
"""
        
        
    
