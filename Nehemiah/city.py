from city_functions import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break

	formatted_city = get_formatted_city(first, last)
	print(f"\tNeatly formatted city name: {formatted_city}.")
