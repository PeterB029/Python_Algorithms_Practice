# Checking Membership (Boolean results)
y = {'pork':25.3, 'beef':33.8, 'chicken':22.7}

#Check membership in y_keys (Only looks in keys, not values)
print('beef' in y)
#output: True

#Checks membership in y_values
print(7 in y.values())
#output: False