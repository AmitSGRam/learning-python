#looping through a dictionary
#looping through all key-value pairs
user_0={
	'username':'efermi',
	'first':'enfrico',
	'last':'fermi'
}
for key, value in user_0.items():
	print(f'\nKey: {key}')
	print(f'value: {value}')
# for k,v in user_0.items():
# 	print(f'\nKey: {k}')
# 	print(f'value: {v}') #this works the same	 
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages:
	print(name.title())

favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

friends=['phil','sarah']
for name in favorite_languages.keys():
	print(f'Hi {name.title()}.')
	if name in friends:
		language = favorite_languages[name].title()
		print(f'\t{name.title()}, I see you love {language}!')
	if 'erin' not in favorite_languages.keys():
		print("Erin, please take our poll!")

#Looping through a dictionary's keys in a particular order

favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

#looping through all values in a dictionary
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

languages1={'python','ruby','python','c'}
print(languages1) 

#Nesting
#A list of dictionaries

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for x in aliens:
	print(x)

#Make an empty list for storing aliens

aliens=[]
#make 30 green aliens
for y in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#show the first 5 aliens
for yy in aliens[:5]:
	print(yy)
print('...')


#changing the color of the first 3 green aliens to yellow, change their speed to medium and points to 10 
for zz in aliens[:3]:
	if zz['color']=='green':
		zz['color']='yellow'
		zz['speed']='medium'
		zz['points']=10
#show the first 5 aliens
for zz in aliens[:5]:
	print(zz)
print('...')