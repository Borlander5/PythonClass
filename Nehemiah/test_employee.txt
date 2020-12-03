import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	
	def setUp(self):
		"""
		Create a survey and a set of response for use in all test methods.
		"""
		question = "Whould you like to change your annual salary?"
		self.my_survey = Employee(salary)
		self.responses = ['no', 'yes']

if __name__ == '__main__':
	unittest.main()