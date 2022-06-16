s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 & s2) #values in both sets
#output: {3}

print(s1 | s2) #values in either sets
#output: {1, 2, 3, 4, 5}

print(s1 ^ s2) #values in one set or other set (NOT in Both)
#output: {1, 2, 4, 5}

print(s1 - s2) #values in s1
#output: {1, 2}

print(s1 <= s2) #checks if s1 is in s2
#output: False

print(s1 >= s2) #checks if s2 is in s1
#output: False