import timeit
from timeit import Timer

class Deque:
 def __init__(self):
    self.items = []
 def is_empty(self):
    return self.items == []
 def add_front(self, item):
    self.items.append(item)
 def add_rear(self, item):
    self.items.insert(0,item)
 def remove_front(self):
    return self.items.pop()
 def remove_rear(self):
    return self.items.pop(0)
 def size(self):
    return len(self.items)
 
def testdeque():
   # initialize deque
   deque = Deque()
   
   item = int()
   #adds a new item to the front of the deque. It needs the item and returns nothing.
   deque.add_front(item)
   
   # adds a new item to the rear of the deque. It needs the item and returns nothing.  
   deque.add_rear(item)
   
   # removes the front item from the deque. It needs no parameters and returns the item. The deque is modified. 
   deque.remove_front() 
   
   # removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified. 
   deque.remove_rear() 
   
   # tests to see whether the deque is empty. It needs no parameters and returns a boolean value. 
   deque.is_empty() 
   
   # returns the number of items in the deque. It needs no parameters and returns an integer. 
   deque.size() 


if __name__ == '__main__':
    t = Timer("testdeque()", "from __main__ import testdeque")
    print("testdeque for 1 million int",t.timeit(number=1000000), "milliseconds")
   
    t = Timer("testdeque()", "from __main__ import testdeque")
    print("testdeque for 10 million int",t.timeit(number=10000000), "milliseconds")
    
    t = Timer("testdeque()", "from __main__ import testdeque")
    print("testdeque for 100 million int",t.timeit(number=100000000), "milliseconds")
   
   

