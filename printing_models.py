#Start with some designs that need to be printed
unprinted_designs=['phone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
	current_design=unprinted_designs.pop()
	print(f"Printing model: {current_design.title()}")
	completed_models.append(current_design)
def show_completed_models(completed_models):
	print(f"The following models have been printed: {completed_models.title()}")
	for completed_model in completed_models:
		print(completed_model)