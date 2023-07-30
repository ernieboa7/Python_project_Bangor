
from tkinter import *
from maze_cordinate import mazecoordinate
graph= {0:[1],
                 1:[0, 2],
                 2:[1, 3],
                 3:[2, 4],
                 4:[3, 5], 
                 5:[4, 6], 
                 6:[5, 7],
                 7:[6, 8],
                 8:[7, 9],
                 9:[8, 10],
                 10:[9, 11], 
                 11:[10, 12],
                 12:[11, 13],
                 13:[12, 14],
                 14:[13, 15], 
                 15:[14]
        }



class MySTACK: # An implementation of a Python stack.
 def __init__(self):
 # Mobilize the queue to an empty stack.
     self.holder = []
 def push(self,val):
 # Add item val onto the start of the stack.
    self.holder.insert(0,val)
 def pop(self):
 # Removing the tail off the stack and returns it value.
    val = None
    try:
        val = self.holder.pop(0)
        if len(self.holder) == 1:
            self.holder = []
        else:
            self.holder = self.holder
    except:
         pass
    return val
 def IsEmpty(self):
 # Returns True if the queue is empty.
    result = False
    if len(self.holder) == 0:
        result = True
    return result

 def display(self):
 # Returns all value in the queue
    print(self.holder)

def DFS(graph,start,end):
    # Traverses the graph using a Breadth First Search starting 
    # from the start node with end being the goal node. Uses a
    # queue to store the nodes that are current leaves at the
    # fringe of the search.
 
    m = MySTACK() # making an empty stack first
    m.push([start]) # adding the start node onto the queue
    while m.IsEmpty() == False: #As long as the queue is not empty
        path = m.pop()  #remove the first list in the queue and store in path
        last_node = path[len(path)-1]
        print (path)
        if last_node == end:
            print ("VALID_PATH : ", path)
        for link_node in graph[last_node]:
            if link_node not in path:
                new_path = []
                new_path = path + [link_node]
                m.push(new_path)

if __name__ == "__main__":
   DFS(graph,0,15)

  
   