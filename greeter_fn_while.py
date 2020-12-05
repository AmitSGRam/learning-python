def get_formatted_name(f,l):
	full_name=f"{f}{l}"
	return full_name.title()
while True:
	print("please tell me your name:")
	f_name:input("first name:")
	l_name:input("last name:")
	formatted_name=get_formatted_name(f_name,l_name)
	print(formatted_name)