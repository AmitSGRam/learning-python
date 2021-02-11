def get_formatted_name(first, middle, last):
	"""Generate a neatly formatted full name"""
	full_name=f"{first} {middle} {last}"
	return full_name.title()
	"""this version works for people with middle name but breaks for people with only first and last names"""