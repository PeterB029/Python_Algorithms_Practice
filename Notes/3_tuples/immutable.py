# Tuples are immutable, but member objects may be mutable. 
# (If a list is an item in the tuple, the list can be changed but not the tuple)

x = (1 , 2, 3)
# del(x[1])  #will fail: cannot remove from tuples.
# x[1]=8   #will fail: cannot update tuples.

y = ([1, 2], 3)
del(y[0][1]) #This will delete 2 from the list w/in the tuple.
print(y)
#output: ([1], 3)

y += (4,) #concatenating 2 tuples together
print(y)
#output: ([1], 3, 4)