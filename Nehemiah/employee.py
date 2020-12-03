import unittest


class Employee:
	"""Collect anonymous answers to a survey question."""
	
	def __init__(self, first_name, last_name, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary
	
	def give_raise(self, raisex=5000):
		self.salary = self.salary + raisex
  
class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.employee = Employee('Nehemiah', 'Borland', 120000)
		
	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(125000, self.employee.salary)
	
	def test_give_custom_raise(self):
		self.employee.give_raise(6000)
		self.assertEqual(126000, self.employee.salary)

if __name__ == '__main__':
	unittest.main()