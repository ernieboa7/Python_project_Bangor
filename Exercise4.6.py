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
 


def pal_checker(a_string):
  char_deque = Deque()
  for ch in a_string:
    char_deque.add_rear(ch)
    still_equal = True
  while char_deque.size() > 1 and still_equal:
     first = char_deque.remove_front()
     last = char_deque.remove_rear()
     if first != last:
        still_equal = False
  return still_equal

def find_palindromes(filename):
   with open(filename, 'r') as f:
        for line in f:
            # Split the line into words
             words = line.split()
             for word in words:
                # Check if the word is a palindrome
                 if len(word) >= 3: #and pal_checker(word):
                     print(word)

#print out the palindrone from the text
print(find_palindromes('palindrome.txt'))




# For Benchmarking




deque = Deque()

import timeit


# measure the time taken to execute the append method
print('add front ', timeit.timeit(lambda: [deque.add_front(i) for i in range(10000)], number=1 ))

# measure the time taken to execute the insert method
print('add rear', timeit.timeit(lambda: [deque.add_rear(i) for i in range(10000)], number=1 ))


#measure the time taken to execute the pop method
print('remove_front', timeit.timeit(lambda: [deque.remove_front() for i in range(10000)], number=1 ))


#measure the time taken to execute the index method
print('remove_rear', timeit.timeit(lambda: [deque.remove_rear() for i in range(10000)], number=1 ))
