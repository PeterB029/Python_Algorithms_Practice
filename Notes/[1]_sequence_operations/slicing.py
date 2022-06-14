#Slicing - slice out substrings, sublist, subtuples using indexes. 

#[start : end-1 : step]

#If not declared…
#start defaults to begining of sequence
#end defaults to end of the sequence
#step defaults to 1

x = 'computer'
#c o m p u t e r
#0 1 2 3 4 5 6 7

print(x[1:4]) 
#start @ 1 : end @ 4-1=3
#output: omp

print(x[1:6:2])
#start @ 1 : end @ 6-1=5 : step 2
#output: opt

print(x[3:])
#start @ 3 
#output: puter

print(x[:5])
#end @ 5-1=4
#output: compu

print(x[-1])
#Negatives start at the right side of sequence
#output: r

print(x[-3:])
#start @ -3 from end (The last 3 elements)
#output: ter

print(x[:-2])
#end before the last 2 elements
#output: comput