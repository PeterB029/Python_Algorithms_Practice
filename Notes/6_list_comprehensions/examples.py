import random

# new_list = [[transform] [sequence] [filter] ]
# Examples: 
# odds = [x for x in range(1) if x%2==1]
# squares = [x**2 for x in under_10]
# nums = [x for x in s if x.isnumerical( )]

#Get values within range: 
under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))
#output: under_10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#With range, it will start at 0 and go to specified num-1
#In this case it went from 0 to 10-1=9

#Get Squared values from under_10
squares = [x**2 for x in under_10]
print('squares: ' + str(squares))
#output: squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# ** is used to calculate powers. i**7 is i to the power of 7

#Get odd numbers using mod in a range
odds = [x for x in range(10) if x%2==1]
print('odds: ' + str(odds))
#output: [1, 3, 5, 7, 9]

#Get multiple of 10s 
ten_x = [x*10 for x in range(10)]
print('ten_x: ' + str(ten_x))
#output: ten_x: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#Get all numbers from a string
s = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in s if x.isnumeric()]
print(s)
print('nums in Text above: ' + ''.join(nums))
#output: nums: 2073
#.join() combines the list into a single string

#Get the index of a list item
names = ['Fushigiro', 'Itadori', 'Nobara', 'Gojo']
idx = [k for k, v in enumerate(names) if v == 'Nobara'] #will be ('Nobara',2)
print('index = ' + str(idx[0]))
#output: index = 2
#enumerate returns key and value(index count) 

#Delete an item from the list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)

#if-else condition in a comprehension
nums = [5, 3, 10, 18, 6, 7]
new_list = [x if x%2==0 else 10*x for x in nums]
print('new_list: ' + str(new_list))
#output: new_list: [50, 30, 10, 18, 6, 70]