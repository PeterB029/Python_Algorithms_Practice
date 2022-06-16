# dictionary = { key : item }

#Create a dictionary with values we set.
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(x)
#output: {'pork':25.3, 'beef':33.8, 'chicken':22.7}

#Create a dictionary with a list of tuples
x = [('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)]
print(x)
#output: {'pork':25.3, 'beef':33.8, 'chicken':22.7}

#Create a dictionary; notice there is no quote around strings.
#Python knows to convert these when the dictionary is made. 
x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x)
#output: {'pork':25.3, 'beef':33.8, 'chicken':22.7}