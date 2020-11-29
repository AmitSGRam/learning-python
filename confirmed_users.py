#start with users that need to be verified
#and an empty list to hold confirmed users
unconfirmed_users=['alice','berus','cersus']
confirmed_users=[]
while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	print(f"The following users are being verified: {current_user.title()}")
	confirmed_users.append(current_user)
print(f"Verified users are:")
for c in confirmed_users:
	print(c.title())