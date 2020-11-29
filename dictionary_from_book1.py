#Starting with an empty dictionary

alien_0={}
alien_0['color']='green'
alien_0['points']=5

print(alien_0)

print('')
#modifying values in a dictionary
alien_0={'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color']='yellow'
print(f"The alien is now {alien_0['color']}.")
print('')
alien_0={'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"original position: {alien_0['x_position']}")  
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"new position of the alien(when alien is medium): {alien_0['x_position']}")

alien_0['speed'] = 'fast'
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"new position of the alien(when alien is fast): {alien_0['x_position']}")
print('')
print(alien_0)

#removing key-value pairs
alien_0={'color':'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

#dictionary with similar objects
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
print(f"Phil's favorite language is {favorite_languages['phil']}")

#using get() to access values

alien_0={'color':'green','speed':'slow'}
# print(alien_0['points']) # if we run this, we'll get result-> KeyError: 'points' . as we haven't assigned a value for the key 'points'

print(alien_0.get('points','No point value assigned.'))
print(alien_0.get('point')) #key doesn't exist, python returns the value 'None' , this is NOT an eror and is a special value meant to indicate the absence of a value
