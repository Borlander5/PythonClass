
class Restaurant:
	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine
		self.number_served = 52762

	def what(self):
		print(f"The name of this restaurant is {self.name}.")

	def serving(self):
		print(f"{self.cuisine}s are now being served!")
	
	def set_number_served(self, worth):
		self.served_number = worth


class IceCreamStand(Restaurant):
	def __init__(self, flavors):
		self.flavors = flavors
	
	def ice_cream(self):
		print(f"{self.flavors} ice cream is now ready!")



Ice_Cream_Stand = IceCreamStand('Caramel Cookie Dough')
Ice_Cream_Stand.ice_cream()


Ice_Cream_Stand = IceCreamStand('Chocolate')
Ice_Cream_Stand.ice_cream()

"""
open_restaurant = Restaurant('IN-N-OUT', 'Cheeseburger')
print(f"{open_restaurant.name} is now open!")
open_restaurant.what()
open_restaurant.serving()

one_restaurant = Restaurant('Texas Roadhouse', 'Steak')
print(f"{one_restaurant.name} is now open!")
one_restaurant.what()
one_restaurant.serving()

two_restaurant = Restaurant('California Pizza Kitchen', 'pizza')
print(f"{two_restaurant.name} is now open!")
two_restaurant.what()
two_restaurant.serving()

three_restaurant = Restaurant('Nowhere', 'Nothing')
print(f"{three_restaurant.name} is now open!")
three_restaurant.what()
three_restaurant.serving()

one_restaurant.number_served = 23
print(f"{one_restaurant.number_served} customers have been served.")

one_restaurant.number_served = 67
print(f"{one_restaurant.number_served} customers have been served.")

two_restaurant.number_served = 6
print(f"{two_restaurant.number_served} customers have been served.")

two_restaurant.number_served = 145
print(f"{two_restaurant.number_served} customers have been served.")

three_restaurant.number_served = 255
print(f"{three_restaurant.number_served} customers have been served.")

three_restaurant.number_served = 14613
print(f"{three_restaurant.number_served} customers have been served.")

restaurant = Restaurant('Burger King', 'Cheeseburger')

restaurant.set_number_served(411)
print(f"{restaurant.number_served} customers have been served.")


"""


