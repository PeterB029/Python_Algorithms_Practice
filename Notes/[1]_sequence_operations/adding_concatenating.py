#Adding/Concatenating - Combine 2 sequences of the same type by using '+'

#string
x = 'Llama' + 'Explorer'
print(x)
#output: LlamaExplorer

#list
y = ['happy','llama'] + ['explorer']
print(y)
#['happy', 'llama', 'explorer']

#tuple
z = ('Itadori', 'Fushigiro', 'Nobara') + ('Gojo',) #Comma after Gojo is needed so Python knows its a tuple. 
print(z)
#('Itadori', 'Fushigiro', 'Nobara', 'Gojo')