import random
import timeit
from timeit import Timer
# Completed implementation of a queue ADT
class Queue:
   def __init__(self):
       self.items = []
   def is_empty(self):
       return self.items == []
   def enqueue(self, item):
       self.items.insert(0,item)
   def dequeue(self):
       return self.items.pop()
   def size(self):
       return len(self.items)
   

def testQueue():
# Number of integers to insert and remove from the stack
   num_integers = int()

#initialize the Queue
   queue = Queue()
# Insert the integers onto the queue
   queue.enqueue(random.randint(0, num_integers))

# Remove the integers from the queue
   queue.dequeue()
   return queue.is_empty()

if __name__ == '__main__':
    t = Timer("testQueue()", "from __main__ import testQueue")
    print("testQueue for 1 million int",t.timeit(number=1000000), "milliseconds")
   
    t = Timer("testQueue()", "from __main__ import testQueue")
    print("testQueue for 10 million int",t.timeit(number=10000000), "milliseconds")
    
    t = Timer("testQueue()", "from __main__ import testQueue")
    print("testQueue for 100 million int",t.timeit(number=100000000), "milliseconds")
   
   