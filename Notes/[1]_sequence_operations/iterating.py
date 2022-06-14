#Iterating - Stepping through the items in a sequence.

#for [variable] in [sequence]:
#      [do something]

#item 
#(variable called item that represents each value in the sequence)
#for each item in the sequence x: print item
x = [7, 3, 12]
for item in x:
	print(item)
#output:
#7
#3
#12

#index & item
#for each index & item in enumerate(y): print index & item
y = [7, 3, 12]
for index, item in enumerate(y):
	print(index, item)
#output
#0 7
#1 3
#2 12