import importlib.util
import sys
spec = importlib.util.spec_from_file_location("module.name", "/run/media/amit/New Volume/lin/python/Classes/car.py")
foo = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = foo
spec.loader.exec_module(foo)
foo.Car('tesla', 'x', 2014)