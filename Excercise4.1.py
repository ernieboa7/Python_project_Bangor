import random
import timeit
from timeit import Timer
# Excercise 4.1
# Completed implementation of a stack ADT
class Stack1:
 def __init__(self):
    self.items = []
 def is_empty(self):
    return self.items == []
 def push(self, item):
    self.items.append(item)
 def pop(self):
    return self.items.pop()
 def peek(self):
    return self.items[len(self.items)-1]
 def size(self):
    return len(self.items)



class Stack2:
 def __init__(self):
    self.items = []
 def is_empty(self):
    return self.items == []
 def push(self, item):
    self.items.insert(0, item)
 def pop(self):
    return self.items.pop(0)
 def peek(self):
    return self.items[0]
 def size(self):
    return len(self.items)

rand_num=0

def testStack1():
    # Testing specific random number
    # initializing the stack
    s1= Stack1()
    
    # push(item) adds a new item to the top of the stack. It needs the item and returns nothing. 
    s1.push(random.randint(0, rand_num))
    
    # pop Remove the integers from the stack
    s1.pop()
    # is_empty tests to see whether the stack is empty.
    s1.is_empty()
    # size returns the number of items on the stack
    s1.size()
    

   
def testStack2():
    # Testing specific random number
    # Testing specific random number
    # initializing the stack
    s2= Stack2()
    
    # push(item) adds a new item to the top of the stack. It needs the item and returns nothing. 
    s2.push(random.randint(0, rand_num))
    
    # pop Remove the integers from the stack
    s2.pop()
    # is_empty tests to see whether the stack is empty.
    s2.is_empty()
    # size returns the number of items on the stack
    s2.size()
    
    
    

if __name__ == '__main__':
    t1 = Timer("testStack1()", "from __main__ import testStack1")
    print("testStack1 for 1 million int",t1.timeit(number=1000000), "milliseconds")

    t2 = Timer("testStack2()", "from __main__ import testStack2")
    print("testStack2  for 1 million int",t1.timeit(number=1000000), "milliseconds")


    t1 = Timer("testStack1()", "from __main__ import testStack1")
    print("testStack1 for 10 million int",t1.timeit(number=10000000), "milliseconds")

    t2 = Timer("testStack2()", "from __main__ import testStack2")
    print("testStack2 for 10 million int",t1.timeit(number=10000000), "milliseconds")  
     

    t1 = Timer("testStack1()", "from __main__ import testStack1")
    print("testStack1 for 100 million int",t1.timeit(number=100000000), "milliseconds")

    t2 = Timer("testStack2()", "from __main__ import testStack2")
    print("testStack2 for 100 million int",t1.timeit(number=100000000), "milliseconds")        