a = [1,3,5,7,9,11]
#[2,6,10,14,18,22]
#inorder to do this we can use append
c = []
for x in a:
	c.append(x*2)
print(c)

#we can use list comprehension to do the same^^
d = [x*2 for x in a]
print(d)

#let's create [1,4,9,16,25,36]

e1 = []
for x in range(1,7):
	e1.append(x**2)
print(e1)

#using list comprehension

e2 = [x**2 for x in range(1,7)]
print(e2)

#et's create [36,25,16,9,4,1]

f1 = [x**2 for x in range(1,7)]
f1.reverse()
print(f1)

f2 = [x**2 for x in range(6,0,-1)]
print(f2)