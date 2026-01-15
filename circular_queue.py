class CircularQueue:
    def __init__(self, size):
        self.size = size
        # if the size is 5 we have  5 slots of none values
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def is_full(self):
        return self.front == (self.rear + 1) %self.size
    
    def is_empty(self):
        return self.front == -1
            
    def enqueue(self, data):
        # Checking if queue is full 
        if self.is_full():
            print("Queue is full")
            return
        
        if self.is_empty():
            # if queue is empty initialize both front and rear
            self.front = 0
            self.rear = 0 
        else:
             # advance the rear circularly 
             self.rear = (self.rear + 1)% self.size

        # store the data at rear position
        self.queue[self.rear]=data
        print(f"Inserted {data}")
    
    def dequeue(self):
        # Checkig if queue is empty
        # if self.front == -1 :
        #     print("Queue is empty nothing to remove")
        if self.is_empty():
            print("Queue is empty nothing to remove")
            return None
        
        # store the removed item so that we can return it 
        removed_element = self.queue[self.front]
        # if the queue contains only one item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front to the next element
            self.front = (self.front + 1) % self.size
            
        print(f"Removed : {removed_element}")
        return removed_element
    
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(12)
cq.enqueue(15)
cq.enqueue(5)
cq.enqueue(1)
cq.enqueue(9)
# print(f"Removed: {cq.dequeue()}")
cq.dequeue()
