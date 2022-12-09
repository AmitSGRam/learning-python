favorite_languages = {
    'sarah' : 'python',
    'johnny' : 'c',
    'silverhand' : 'c++',
    'vettori' : 'java'
}
sarah_favlang = favorite_languages['sarah'].title()
print(f"the favorite language of sarah is {sarah_favlang}")
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
yamada_lang = favorite_languages.get('yamada', 'he isn\'t in the list')
print(f"is yamada in the list?\nNo, {yamada_lang}")
for name, lang in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {lang.title()}")
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

for values in favorite_languages.values():
    print(f"values of the list is : {values}")
    
for values in set(favorite_languages.values()):
    print(f"set of the values in the list is : {values}")

set_1 = {'python', 'c', 'c++', 'python'}
print(set_1)