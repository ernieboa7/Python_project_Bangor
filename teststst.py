
from tkinter import *
from maze import draw_hampton_court_maze as maze

mazecoordinate = [(190,-140),
                 (190,-130),
                 (-170, -130),
                 (-170, 70),
                 (190,70), 
                 (190, -110), 
                 (-150, -110),
                 (-150, 50),
                 (170, 50),
                 (170, -90),
                 (-130, -90), 
                 (-130, 30),
                 (150, 30),
                 (150, -70),
                 (10, -70), 
                 (10, -60)]
        

mazegraph1= {(190,-140):[(190,-130)],
             (190,-130):[(190,-140), (-170, -130)],
                 (-170, -130):[(190,-130), (-170, 70)],
                 (-170, 70):[(190,-130), (190,70)],
                 (190, 70):[(190,-130), (190, -110)], 
                 (190, -110):[(190,70), (-150, -110)], 
                 (-150, -110):[(190, -110), (-150, 50)],
                 (-150, 50):[(-150, -110), (170, 50)],
                 (170, 50):[(-150, 50), (-130, -90)],
                 (-130, -90):[(170, 50), (-130, 30)],
                 (-130, 30):[(-130, -90), (150,30)], 
                 (150, 30):[(-130, 30), (150,-70)],
                 (150,-70):[(150,30), (10,-70)],
                 (10,-70):[(150, 30), (10, -60)],
                 (10, -60):[]
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

def DFS(graph, start, end):
    ''' Traverses the graph using a Depth First Search starting 
        from the start node with end being the goal node. Uses a
        stack to store the nodes that are current leaves at the
        fringe of the search.'''
 
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



class MyQUEUE: # Implementation of a queue.
    def __init__(self):
        # Initialises the queue to an empty queue.
        self.holder = []
    def enqueue(self,val):
        # Appends item val onto the end of the queue.
        self.holder.append(val)
    def dequeue(self):
        # Pops the head off the queue and returns it value.
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
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

def BFS(graph,start,end):
    ''' Traverses the graph using a Breadth First Search starting 
   from the start node with end being the goal node. Uses a
   queue to store the nodes that are current leaves at the
   fringe of the search.'''
    
    q = MyQUEUE() # make an empty queue first
    q.enqueue([start]) # add the start node onto the queue

    while q.IsEmpty() == False:
        path = q.dequeue()
        last_node = path[len(path)-1]
        print (path)
        if last_node == end:
            print ("VALID_PATH : ", path)
        for link_node in graph[last_node]:
            if link_node not in path:
                new_path = []
                new_path = path + [link_node]
                q.enqueue(new_path)



start = (190, -140)
end= (10, -60)


if __name__ == "__main__":
    
    done = False
    while not done:
        done = True
        algorithm = input("Select algorithm (1 to 2): ")
        if algorithm == '1':
            BFS(mazegraph1, start, end)
        elif algorithm == '2':
            DFS(mazegraph1,start,end)
maze(1, "green", 20, 4, 180, -160)       
 
