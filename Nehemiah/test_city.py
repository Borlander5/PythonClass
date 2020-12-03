import unittest
from city_functions import get_formatted_city

class NamesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Do names like "Atascadero America' work?"""
		formatted_city = get_formatted_city('Atascadero', 'Atascadero')
		self.assertEqual(formatted_city, 'Atascadero Atascadero')

	def test_first_last_population(self):
		formatted_city = get_formatted_city(
			'louisville', 'America', '1000000')
		self.assertEqual(formatted_city, 'Louisville America 1000000')

if __name__ == '__main__':
	unittest.main()
