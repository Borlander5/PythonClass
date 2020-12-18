class Settings:
	"""A class to store all settings for Alien Invaion."""
	def __init__(self):
		"""Intiialize the game's settings."""

		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230,)

		#Ship Settings
		self.ship_speed = 1.5

		#Bullet Settings
		self.bullet_speed = 10.0
		self.bullet_width = 1200
		self.bullet_height = 2
		self.bullet_color = (0, 255, 0)
		self.bullets_allowed = 55