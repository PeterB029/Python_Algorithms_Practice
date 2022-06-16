#gives us a new empty tuple
x = ()
print(x)

#we can pass in items we want in the tuple
x = (1, 2, 3)
print(x)

#The parenthesis are optional, Python knows if you use commas 
x = 1, 2, 3
print(x)

#Tuples can have 1 item, we just need to include the comma to let Python know
x = 1,
print(x, type(x))
#output: (2,) <class 'tuple'>

#You can also convert a list into a tuple
list1 = [2, 4, 6]
x = tuple(list1)
print(x, type(x))
#output: (2, 4, 6) <class 'tuple'>