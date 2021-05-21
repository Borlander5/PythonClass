import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
from datetime import date, timedelta, datetime


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        #Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_number = 1


        self._create_alien_boss()

        self.play_button = Button(self, "Let's Go!")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

    def _update_bullets(self):
        """Update positon of bullets and get rid of old bullets."""
        #Update bullet positions.
        self.bullets.update()
        self.alien_bullets.update()

        #Get rid of bullets thave have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        #Get rid of bullets thave have disappeared.
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top >= self.settings.screen_height:
                self.alien_bullets.remove(bullet)
            
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet_alien collisions."""
        #Remove any bullets and aliens that have collided.
        AliveAliens = pygame.sprite.Group()
        for alien in self.aliens:
            if alien.alive == True:
                AliveAliens.add(alien)

        collisions = pygame.sprite.groupcollide(self.bullets, AliveAliens, True, False)

        if collisions:
            #self.alien.image = pygame.image.load("Aliens1\\images\\boom.bmp")
            #self.alien.rect = self.alien.image.get_rect()
            #self._update_aliens

            for aliens in collisions.values():
                for alien in aliens:
                    if alien.alive:
                        self.stats.score += self.settings.alien_points
                        alien.explode()
            self.sb.prep_score()
            self.sb.prep_ships()
            self.sb.check_high_score()
       
        if not self.aliens:
            #Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_alien_boss()

    def _check_events(self):
        """Respond to kewpresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
                
            self.aliens.empty()

            self.bullets.empty()
            self.alien_bullets.empty()

            self._create_alien_boss()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit(0)
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, False, self.ship)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        #Make the most recenlty drawn screen visible.
        pygame.display.flip()

    def _create_alien_grid(self):
        """Create the fleet of aliens."""
        #Create an alien and find the number of aliens in a row. 
        #Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        for yloc in range(number_rows):
            for xloc in range(number_aliens_x):
                self._create_alien(xloc, yloc)
        
    def _create_alien_boss(self):
        for alien_quantity in range(1, self.alien_number):
            self._create_alien(alien_quantity * 100, 150, self.alien_number / 5)

        self.alien_number += 1

    def _create_alien(self, xloc, yloc, alien_speed):
        """Create an alien and place in in the row."""
        alien = Alien(self)
        #alien_width, alien_height = alien.rect.size
        alien.x = xloc
        alien.y = yloc
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        alien.alien_speed = alien_speed
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update the positions of all aliens in the fleet."""
        #self._check_fleet_edges()
        self.aliens.update()
        
        for alien in self.aliens:
            if alien.alive == False and datetime.now() >= alien.destroyAfter:
                self.aliens.remove(alien)
            elif alien.alive == True and alien.WannaFire():
                new_bullet = Bullet(self, True, alien)           
                self.alien_bullets.add(new_bullet)

        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #Decrement ships left.

            self.stats.ships_left -= 1
            self.sb.prep_ships()
            #Get rid of any remaining aliens and bullets.

            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_alien_boss()
            self.ship.center_ship()

            #Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit.
                self._ship_hit()
                break


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()