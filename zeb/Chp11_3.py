class Employee:
	
	def __init__(self, firstname, lastname, salary):
		self.f_name = firstname
		self.l_name = lastname
		self.salary = salary

	def give_raise(self, amount=5000):
		self.salary = self.salary + amount