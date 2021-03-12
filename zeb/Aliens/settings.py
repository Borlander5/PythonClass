class Settings:
	"""A class to store all settings for Alien Invaion."""
	def __init__(self):
		"""Intiialize the game's settings."""

		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230,)

		#Ship Settings
		self.ship_speed = 6.5
		self.ship_limit = 3

		#Bullet Settings
		self.bullet_speed = 7.0
		self.bullet_width = 9000
		self.bullet_height = 5
		self.bullet_color = (230, 230, 230)
		self.bullets_allowed = 55

		# Alien Settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		#fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		# How quickly the game speeds up 
		self.speedup_scale = 1.2
		self.initialize_dynamic_settings()
		# How quickly the alien point values increase
		self.score_scale = 1.5

	def initialize_dynamic_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		#fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		#Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)