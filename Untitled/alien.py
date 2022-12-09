alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])

print(alien_0['points'])

new_points = alien_0['points']
print(f"you now have {new_points} points!!")

alien_0['x_position'] = 1
alien_0['y_position'] = 2

x_pos = alien_0['x_position']
y_pos = alien_0['y_position']

print(f"the alien is now at {x_pos},{y_pos}")

print(f"the dictionary is now {alien_0}")

alien_0['speed'] = 'medium'

print(f"x position of the alien is now {x_pos}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"\n The latest location of the alien is now {alien_0['x_position']},{alien_0['y_position']}")

alien_0['delete_this'] = 'some value'
print(alien_0['delete_this'])
print(alien_0)
del(alien_0['delete_this'])
print(alien_0)