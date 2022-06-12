# Index - Returns the index of the first occurence of an item.

# index(item) ⇒ returns the index of the first time the item occurs

#string
x = 'llama'
print(x.index('l'))
#output: 0
#the first 'l' encountered is @ index 0

#list
y = ['happy', 'llama', 'explorer']
print(y.index('explorer'))
#output: 2
#the first 'explorer' is encountered @ index 2

#tuple
z = ('Itadori', 'Fushigiro', 'Nobara', 'Gojo')
print(z.index('Gojo'))
#output: 3
#the first 'Gojo' is encountered @ index 3