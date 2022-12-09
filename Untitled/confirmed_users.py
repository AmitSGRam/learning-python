#Start with uers that need to be verified,
#and an empty list to hold confirmed users.abs

unconfirmed_users = ['ben','candace','colby']
confirmed_users = []

"""verify each user until there are no more unconfirmed users.
Moved each verified user into the list of confirmed users."""

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display all confirmed users.
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"\nConfirmed users are: {confirmed_user.title()}")