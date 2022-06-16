#We can pass in items we want in our set.
x = {3, 5, 3, 5}
print(x) #duplicates are filtered out.
#output: {3, 5}

#This creates an empty set. 
y = set()
print(y)
#output: set()

#A list can be turned into a set.
list1 = [2, 3, 4]
z = set(list1)
print(z)
#output: {2, 3, 4}