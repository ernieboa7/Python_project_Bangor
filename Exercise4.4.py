import random

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

def simulate(numCars, behavior):
# initialize the queue
    queue = Queue()
    # compute the total wait time for all cars
    total_wait_time = int()
    # Iterate over the number of cars
    for car in range(numCars):
        # Each car has a random arrival time between 0 and 5 seconds
        arrival_time = random.uniform(0, 5)
        # If the behavior is 1 (change lanes), add the car to the queue and update the wait time
        if behavior == 1:
            queue.enqueue(arrival_time)
            total_wait_time += queue.size() * arrival_time
            # If the behavior is 2 (stay in lane), only add the car to the queue if it's empty
        elif behavior == 2:
            if queue.is_empty():
                queue.enqueue(arrival_time)
            else:
                 total_wait_time += arrival_time
                 # Return the average wait time for all cars
        avg_waiting_time = total_wait_time/numCars             
    return avg_waiting_time

# Simulate behavior 1 for 1000 cars
avg_wait_time_1 = simulate(1000, 1)
print("Average wait time for behavior 1:", avg_wait_time_1,'in milliseconds')

# Simulate behavior 2 for 1000 cars
avg_wait_time_2 = simulate(1000, 2)
print("Average wait time for behavior 2:", avg_wait_time_2 ,'in milliseconds')

# To determine which behavior has a shorter average wait time
if avg_wait_time_1 < avg_wait_time_2:
    print("Behavior 1 has a shorter average waiting time than behaviour 2.")
else:
    print("Behavior 2 has a shorter average waiting time than behaviour 1.")