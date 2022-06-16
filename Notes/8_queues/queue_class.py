from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item): #adds item to end of the line
        self.queue.append(item)

    def dequeue(self): #removes item from front of the line
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    
    def __str__(self): #print out the queue as a string
        return str(self.queue)

my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(10)
print(my_queue)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())