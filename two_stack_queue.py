class TwoStackQueue:
    def __init__(self, max_size):
        # stack for enqueue operations
        self.stack1 = []
        #stack for dequeue operations
        self.stack2 = []
        # size definition
        self.max_size = max_size 

    def is_full(self):
        # Total elements in queue = elements in both stacks
        return len(self.stack1) + len(self.stack2) == self.max_size
    
    def is_empty(self):
        # Checking if both stacks are empty
        return not self.stack1 and not self.stack2

    def enqueue(self, data):

        if self.is_full():
            print("Queue is full")
            return
        self.stack1.append(data)
        print(f"Inserted {data}")

    def dequeue(self):
    # Checking if both stacks are empty
        if self.is_empty():
            print("Queue is empty")
            return None 
        
        # if stack2 is empty then transfer all elements to stack 2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # now remove elements from stack 2
        return self.stack2.pop()
    
        
tq = TwoStackQueue(10)

tq.enqueue(10)
tq.enqueue(20)
tq.enqueue(30)
print(tq.dequeue())  
print(tq.dequeue()) 
