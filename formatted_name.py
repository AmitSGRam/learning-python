def get_formatted(first_name,middle_name,last_name):
	full_name=f"{first_name} {middle_name} {last_name}"
	return full_name.title()
musician = get_formatted('ludwig','van','beethoven')
print(musician)