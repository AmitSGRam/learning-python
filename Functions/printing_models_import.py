from printing_models_fn1 import print_models as pm
from printing_models_fn1 import show_completed_models as show
#from printing_models_fn1 import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs[:], completed_models)
show(completed_models)