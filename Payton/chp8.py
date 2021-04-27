def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")

greet_user('payton')



def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'milo')  
describe_pet('dog', 'rocko')
describe_pet('fish', 'goldie')



def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

celebrity = get_formatted_name('payton', 'forrest', 'knudson')
print(celebrity)

artist = get_formatted_name('chole', 'walker')
print(artist)




def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First Name: ")
	if f_name == 'q':
		break

	l_name = input("Last Name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")