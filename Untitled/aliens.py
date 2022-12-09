alien_0 = {
    'color' : 'green',
    'points' : 5
}
alien_1 = {
    'color' : 'red',
    'points' : 10
}
alien_2 = {
    'color' : 'blue',
    'points' : 15
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

# make 30 green aliens.

for alien in range(30):
    new_alien = {        
        'color' : 'green',
        'points' : 10,
        'speed' : 'slow'
    }
    aliens.append(new_alien)

for alien in aliens[2:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
# make the first 3 aliens yellow
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 20
        alien['speed'] = 'fast'

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"\nTotal number of aliens = {len(aliens)}")