from city_place import get_city_country

print("Enter 'q' at any time to quit."
while True:
	city = input("Please give me a city: ")
	if city == 'q':
		break
	country = input("Please give me a country: ")
	if country == 'q':
		break

	city_country = get_city_country(city, country)
	print(f"{city_country}")