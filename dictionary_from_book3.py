aliens=[]
#make 30 green aliens
for y in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#show the first 5 aliens
for yy in aliens[:5]:
	print(yy)
print('...')
for zzz in aliens[3:9]:
	for y in aliens[6:9]:
		if y['color']=='green':
			y['color']='yellow'
			y['speed']='medium'
			y['points']=10
	if zzz['color']=='green':
		zzz['color']='yellow'
		zzz['speed']='medium'
		zzz['points']=10
	elif zzz['color']=='yellow':
		zzz['color']='red'
		zzz['speed']='fast'
		zzz['points']=15

for k in aliens[:9]:
	print(k)
print('...')