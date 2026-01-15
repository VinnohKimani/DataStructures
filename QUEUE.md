# Circular Queue (Data Structures & Algorithms)

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
