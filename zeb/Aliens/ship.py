import pygame

class Ship:
    """ A class to manage the ship """
    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:\\Users\\Kids\\source\\repos\\PythonClass\\zeb\\Aliens\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the Screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Store a decimal calue for the ship's horizontal position
        self.x = float(self.rect.x)
        # Movement Flag
        self.moving_right = False
        self.moving_left = False
   
    def update(self):
        """Update the ship's position based on movement flags."""
        #Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #Update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)