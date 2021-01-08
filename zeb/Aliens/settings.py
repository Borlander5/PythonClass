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
		self.alien_speed = 5.0
		self.fleet_drop_speed = 10
		#fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1