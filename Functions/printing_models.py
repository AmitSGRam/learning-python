#Start with some designs that need to be printed.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_designs = []

#simulate printing each design, until none are left.
#Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Pring model: {current_design}")

#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_designs:
    print(completed_model)