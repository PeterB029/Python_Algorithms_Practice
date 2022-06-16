# Iterating a dict (Note: Items are in random order. Dictionaries are unordered)

y = {'pork':25.3, 'beef':33.8, 'chicken':22.7}

for key in y:
	print(key, y[key])
	#output: 
	#pork 25.3
	#beef 33.8
	#chicken 22.7

for key, value in y.items():
	print(key, value)
	#output: 
	#pork 25.3
	#beef 33.8
	#chicken 22.7