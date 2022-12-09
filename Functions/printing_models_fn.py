def print_models(unprinted_designs, completed_models):
    #simulate printing each design, until none are left.
    #Move each design to completed_models after printing.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Pring model: {current_design}")
        completed_models.append(current_design)

#Display all completed models.
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("\n")
print("1-------------------------------------------")
print(unprinted_designs)
print(completed_models)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models) #using [:] makes a copy of the list to send to the function. use it to avoid emptying the unprinted list.
show_completed_models(completed_models)

print("\n")
print("2-------------------------------------------")
print(unprinted_designs)
print(completed_models)