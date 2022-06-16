#Delete item from Dictionary
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7, 'shrimp':38.2}

#DELETE ONE ITEM
del(x['shrimp']) #Deletes both key:value
print(x)
#output: {'pork':25.3, 'beef':33.8, 'chicken':22.7}

#DELETE ALL ITEMS
x.clear()
print(x)
#output: {}

#DELETE THE DICTIONARY ITSELF
del(x)