def print_models(unprinted_designs,completed_designs):
	while unprinted_designs:
		current_designs=unprinted_designs.pop()
		print(f"Printing Model: {current_designs.title()}")
		completed_designs.append(current_designs)
def show_completed_models(completed_designs):
	print("\nThe following models have been printed:")
	for completed_design in completed_designs:
		print(completed_design)
unprinted_designs=['phone case','robot pendant','dodecahedron']
completed_designs=[]

print_models(unprinted_designs,completed_designs)
show_completed_models(completed_designs)