#using variables in string
first_name="wolfgang"
last_name="mozart"
full_name=f"{first_name} {last_name}"
print(full_name.title())

#using format f"{}{}"
first="ludvig"
last="beethoven"
full=(f"{first} {last}")
other=f'Have you guys heard about {full.title()}?'
print(other)