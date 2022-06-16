# A stack is a Last-In-First-Out (LIFO) data structure

#Stack concept using List operations:
my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack)
#output: [4, 7, 12, 19]
print(my_stack.pop())
print(my_stack.pop())
print(my_stack)
#output: 
#19
#12
#[4, 7]

#Creating a wrapper class for Stack using List operations but creating our own methods.
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item): #push an item onto the stack
        self.stack.append(item)

    def pop(self): #pop and item off of the stack
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self): #look at the item on top of the stack without removing it
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self): #print out the stack as a string
        return str(self.stack)

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
print(my_stack)
#output: [1, 3]

print(my_stack.pop())
#output: 3

print(my_stack.peek())
#output: 1

print(my_stack.pop())
#output: 1

print(my_stack.pop())
#output: None