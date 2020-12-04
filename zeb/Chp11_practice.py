def city_country(city, country, population=''):
	if population:
		location = f"{city} {country} {population}"
	else:
		location = f"{city} {country}"
	return location.title()