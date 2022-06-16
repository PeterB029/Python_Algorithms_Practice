# Accessing Keys and Values in a dict. (Note: Not compatible with Python 2)
y = {'pork':25.3, 'beef':33.8, 'chicken':22.7}

print(y.keys())    #prints List of all keys
#output: dict_keys(['pork', 'beef', 'chicken'])

print(y.values())  #prints List of all values
#output: dict_values([25.3, 33.8, 22.7])

print(y.items())   #prints List of tuples of key:value pairs
#output: dict_items([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])