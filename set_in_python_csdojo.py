# learning sets in python

# set is a type of data that stores a set of things. unique things

#on a set {1,3} if we try to add {3} to the original set, we'll still get {1,3} as python rejects duplicate elements

a = set()
print(a)

#adding elements to the set

a.add(1)
print(a)
#curly brackets showing the set containing 1

a.add(2)
print(a)

#we get {1,2}
#let's try to add another 2 to the set a

a.add(2)
print(a)

#1 of the useful things to do with a set in python is we can iterate over every element in the set

for x in a:
	print(x)

#we get the same as a list

#we can remove duplicates from a given list

given_list = [1,1,2,2,4]

new_set1 = set()
for x in given_list:
	new_set1.add(x)
print(new_set1)

new_list2 = list(set(given_list))
print(new_list2)
#we got rid off the duplicates of 1,2 and we get {1,2,4}
#create a list of the set
#we can also use new_list = list()
new_list = []
for x in new_set1:
	new_list.append(x)
print(new_list)

#we can add things to a set that are not integers

b = set()
b.add('apple')
b.add('banana')
b.add(5)
b.add('coconut')
print(b)

#find sum of unique elements in given_list2=[1,3,4,1,3]
given_list2 = [1,3,4,1,3]
sum_of_given_list2 = sum(set(given_list2))
print(sum_of_given_list2)

#we can also do the traditional way

new_set2 = set()
for x in given_list2:
	new_set2.add(x)
total = 0
for x in new_set2:
	total += x
print(total)

#completed!!