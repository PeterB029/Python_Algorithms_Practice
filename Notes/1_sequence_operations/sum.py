#Sum - find the total sum of items in a sequence.
#Entire sequence MUST be numeric.

#string => error
#x = [5, 7, 'cat']
#print(sum(x)) => generate an error

#list
y = [2, 5, 8, 12]
print(sum(y))
#output: 27
#2 + 5 + 8 + 12
print(sum(y[-2:]))
#output: 20
#8 + 12

#tuple
z = (50, 4, 7, 19)
print(sum(z))
#output: 80