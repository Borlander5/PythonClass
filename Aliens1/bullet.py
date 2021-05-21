import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
        """A class to manage bullets fired from the ship."""

        def __init__(self, ai_game, alien_bullet, shooter):
            """Create a bullet object at the ship's current position."""
            super().__init__()
            self.screen = ai_game.screen
            self.settings = ai_game.settings
            self.color = self.settings.bullet_color
            self.alien_bullet = alien_bullet

            #Create a bullet rect at (0, 0) and then set correct position.
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
            self.rect.midtop = shooter.rect.midtop
            

            #Store the bullet's position as a decimal value.
            self.y = float(self.rect.y)
        
        def update(self):
            """Move the bullet up the screen."""
            #Update the decimal position of the bullet.
            if self.alien_bullet == True:
                self.y += self.settings.bullet_speed
            else:
                self.y -= self.settings.bullet_speed

            #Update the rect position.
            self.rect.y = self.y

        def draw_bullet(self):
            """Draw the bullet to the screen."""
            pygame.draw.rect(self.screen, self.color, self.rect)