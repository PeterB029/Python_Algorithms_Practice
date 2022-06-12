#Sorting - returns a NEW list of items in sorted order.
#Does NOT change the original list!

#string
x = 'bug'
print(sorted(x))
#output: ['b', 'g', 'u']

#list
y = ['pig', 'cow', 'horse']
print(sorted(y))
#output: ['cow', 'horse', 'pig']

#tuple
z = ('Itadori', 'Fushigiro', 'Nobara', 'Gojo')
print(sorted(z))
#output: ['Fushigiro', 'Gojo', 'Itadori', 'Nobara']

# NOTE: The results provided are a LIST regardless of what it was originally (string, tuple). The original is untouched and a new list is returned. 


# Sorting by 2nd Letter
# Add a key parameter and a lambda function to return the second character.
# (The word key here is a defined parameter name, k is an arbitrary variable name).
z = ('Itadori', 'Fushigiro', 'Nobara', 'Gojo')
print(sorted(z, key=lambda k: k[1]))
#output: ['Nobara', 'Gojo', 'Itadori', 'Fushigiro']
#for each item k, we are comparing the second letter k[1] (index 1, not 0)