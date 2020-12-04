def get_formatted_city(first, last, population=''):
	if population:
		full_name = f"{first} {last} {population}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()