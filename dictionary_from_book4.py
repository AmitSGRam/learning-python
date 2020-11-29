#A list in a dictionary

#store information about a pizza being ordered

pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
}
#summarize the order
print(f"You ordered a {pizza['crust'].title()} - Crust Pizza"
" with the following toppings:") #print(f"You ordered a {pizza['crust']} - crust pizza with the following toppings:") does the same thing

for t in pizza['toppings']:
	print(f"\t{t.title()}")

favorite_languages={
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}
for n,l in favorite_languages.items():
	print(f"\n{n.title()}'s favorite languages are:")
	for language in l:
		print(f"\t{language.title()}")