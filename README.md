# Circular Queue and Two Stack Queue (Data Structures & Algorithms) 
### (using python)

## Overview
A **Circular Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.  
The **last position is logically connected back to the first position**, forming a circular structure.  
This design **eliminates wasted space** that occurs in a linear queue after dequeue operations and prevents **false overflow**.

---

## Characteristics
- Uses a **fixed-size array** (the size must be defined in advance)
- It Ensures **efficient memory utilization**
- It Supports **wrap-around behavior** using **modulo arithmetic**
- It Prevents **false overflow** seen in linear queues
- It Maintains **constant-time operations** for insertion and deletion

---

## Components
- **front**: This is index pointing to the first element in the queue  
- **rear**: This is index pointing to the last element in the queue  
- **size**: This is the maximum number of elements the queue can hold  

---

## Operations
 
- **enqueue** : insertion of elements.
- **dequeue** : removal of element.

---

## Two Stack Queue

## Brief 
- Standard Queues follow the **FIFO** principle: the first item added is the first one removed.
- Standard Stacks follow the **LIFO** principle: the last item added is the first one removed.
- A **Two Stack Queue** technique where  two stack data structures (LIFO) are used together to implement queue behavior (FIFO).
- A max size is defined since the without it the two stacks are dynamically updated
- Two stacks are created stack1 for enqueue operations and stack2 for dequeue operations
- **Stack 1** always stores newly added elements

---

## Operations
### **enqueue**
   - When an element is enqueued, it is pushed directly onto **Stack 1**.
   - This operation is simple and efficient because no rearrangement is required at this stage.
   
### **dequeue**
   - If **Stack 2 is not empty**, the top element of Stack 2 is popped and returned.
   - If **Stack 2 is empty**, all elements from Stack 1 are popped and pushed onto Stack 2.
   - After the transfer, the top element of Stack 2 is popped and returned.