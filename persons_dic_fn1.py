def build(first_name,last_name,age=None):
	full_name={'first':first_name,'last':last_name}
	if age:
		full_name['age']=age
		return full_name
musician=build('ludwig','beethovan',27)
print(musician)