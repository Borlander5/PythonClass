import pygame
import math
import time


from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load("Nehemiah\\Aliens\\images\\unnamed.bmp")
        self.rect = self.image.get_rect()

        
        #Start each new alien near the top left of the screen.
        
        #self.rect.x = self.rect.width
        
        #self.rect.y = self.rect.height
        

        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.path = 1
        self.pathCount = 0
        self.yDirection = 1
        self.xDirection = 1
        self.fake_bottom = 300
        self.alien_speed = 1

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self): 
        self.x += self.xDirection * self.alien_speed
        self.y += self.yDirection * self.alien_speed
        self.fake_bottom += 0.1

        self.rect.y = self.y
        self.rect.x = self.x 

        screen_rect = self.screen.get_rect()

        if self.y >= self.fake_bottom or self.y <= 0: 
            self.yDirection *= -1
        elif self.x >= (screen_rect.right - 50):
            self.xDirection += -1
        elif self.x <= 0:
            self.xDirection += 1
        
 
    """
    def update(self):        
        if self.path == 1: 
            self.x += (self.settings.alien_speed * self.settings.fleet_direction)
            self.y += (self.settings.alien_speed * self.settings.fleet_direction)

        elif self.path == 2:
            self.x -= (self.settings.alien_speed * self.settings.fleet_direction)
            self.y -= (self.settings.alien_speed * self.settings.fleet_direction)        
        elif self.path == 3:
            self.y += (self.settings.alien_speed * self.settings.fleet_direction)    

        elif self.path == 4:
            self.y -= (self.settings.alien_speed * self.settings.fleet_direction)           
            self.x += (self.settings.alien_speed * self.settings.fleet_direction)
            
        elif self.path == 5:
            self.y += (self.settings.alien_speed * self.settings.fleet_direction) 
            self.x += (self.settings.alien_speed * self.settings.fleet_direction)

        elif self.path == 6:
            self.y -= (self.settings.alien_speed * self.settings.fleet_direction) 
            self.x -= (self.settings.alien_speed * self.settings.fleet_direction)
        
        elif self.path == 7:
            self.y += (self.settings.alien_speed * self.settings.fleet_direction) 

        elif self.path == 8:
            self.x -= (self.settings.alien_speed * self.settings.fleet_direction)

        elif self.path >= 9:
            self.y += (self.settings.alien_speed * self.settings.fleet_direction) 
               
                
        if self.path == 9:
            if self.pathCount == self.check_edges():
                self.path += 1
                self.pathCount = 0
        else:
            self.pathCount += 1
            if self.pathCount >= 450:
                self.path += 1
                self.pathCount = 0

        self.rect.y = self.y
        self.rect.x = self.x 
    """        
    
















































































































































































