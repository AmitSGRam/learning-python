print(type("microsoft"))
print(type(True))
print(type(4))
print("")
a=3
b=1
if a>b:
	print("a is greater than b")
	print("")
	if True:
		print("a is greater\n_______________________\n")
boo_value = a>b
print(boo_value)
print("")
c=10
if a>c:
	print("a is greater")
elif a<c:
	print("a is not greater than c")

def are_you_sad(is_rainy, has_umbrella):
	return is_rainy and not has_umbrella

	# if is_rainy == True and not has_umbrella:
	# 	return True
	# else:
	# 	return False

#or

	# if is_rainy == True and has_umbrella == False:
	# 	return True
	# else:
	# 	return False

print(are_you_sad(True, False))
print("")
print(are_you_sad(True, True))

print("")

def c_greater_than_d_plus_e(c,d,e):
	return c>d+e
	# if c > d+e
	# 	return True
	# else:
	# 	return False
print(c_greater_than_d_plus_e(3,1,1))
print("")
print(c_greater_than_d_plus_e(3,1,2))
print("")