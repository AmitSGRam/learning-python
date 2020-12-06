def build_user(first,last,**user_info):
	"""build a dictionary containing everything we know about a user"""
	user_info['first']=first
	user_info['last']=last
	return user_info
user=build_user('albert','einstein',location='princeton',field='physics')
print(user)