class Node:
  def __init__(self, init_data):
      self.data = init_data
      self.next = None
  def get_data(self):
      return self.data
  def get_next(self):
      return self.next
  def set_data(self, new_data):
      self.data = new_data
  def set_next(self, new_next):
      self.next = new_next
      
class UnorderedList:
    def __init__(self):
        self.head = None 
    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count  
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found        
  
    def append(self, item):
        new_node = Node(item)
        if self.head is None:
           self.head = new_node
           return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            last_node.next = new_node
#function to insert an item to a position in the linkedlist
    def insert(self, item, pos):
        new_node = Node(item)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            if count == pos:
                prev_node.next = new_node
                new_node.next = cur_node
                break
            prev_node = cur_node
            cur_node = cur_node.next
#function to find the index of an item in the linkedlist
    def index(self, item):
        count = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == item:
                return count
            cur_node = cur_node.next
            count += 1
        return None
#function to pop an item in the linkedlist
    def pop(self, pos):
        if pos == 0:
            self.head = self.head.next
            return
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            if count == pos:
                prev_node.next = cur_node.next
                return
            prev_node = cur_node
            cur_node = cur_node.next
        return None
#function to find the index of an item in the linkedlist
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
list = UnorderedList()
print(list.is_empty())
list.add(10)
print(list.search(10))
print(list.is_empty())
list.append(45)
print(list.size())
list.insert(50, 0)
print(list.size())
list.pop(2)
print(list.print_list())
print(list.index(25))    


#For Benchmarking
import timeit


# measure the time taken to execute the append method
print('add for 1 million', timeit.timeit(lambda: [list.append(i) for i in range(1000000)], number=1 ))

# measure the time taken to execute the insert method
print('insert for 1 million', timeit.timeit(lambda: [list.insert(i, 100) for i in range(1000000)], number=1 ))


#measure the time taken to execute the pop method
print('pop for 1 million', timeit.timeit(lambda: [list.pop(i) for i in range(1000000)], number=1 ))


#measure the time taken to execute the index method
print('index for 1 million', timeit.timeit(lambda: [list.index(i) for i in range(1000000)], number=1 ))
