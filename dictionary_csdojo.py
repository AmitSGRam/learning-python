#create dictionary

d ={} # or d = dict()

#we can predefine values in a dictionary by s={"pink":10, "red":1}

d["White"] = 100
d["Yellow"] = 200
d["Blue"] = 300

print(d["Blue"])

#keys are commonly strings or numbers

d[10] = 1000
print(d[10])

#how to iterate over key-value pairs:

for key, value in d.items():
	print("key:")
	print(key)
	print("value:")
	print(value)
	print("")