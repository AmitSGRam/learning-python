from pizza_fn2 import *	#importing all functions in a module, making it so that you can call each function without using .	#from module_name import *
make_pizza(16,'pepperoni')
make_pizza(11,'pepperoni','mushroom','cheese')

#it's best not to use this approach when you're working with larger modules you didn't write: if the module has a function name that matches an existing name in your project, you can get some unexpected results.