'''
622. Design Circular Queue

Design your implementation of the circular queue.
The circular queue is a linear data structure in which the operations are
performed based on FIFO (First In First Out) principle and the last position
is connected back to the first position to make a circle. 
It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the 
spaces in front of the queue. In a normal queue, once the queue becomes full,
we cannot insert the next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

Example 1:
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:
    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
 
Follow up: Could you solve the problem without using the built-in queue? 
'''
# Runtime: 68 ms        Your runtime beats 73.20 % of python3 submissions.
# Memory Usage: 14.8 MB Your memory usage beats 47.93 % of python3 submissions.

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.circularQueue = [0] * k
        self.currentSize = 0
        self.frontPointer = None
        self.rearPointer = None


    def enQueue(self, value: int) -> bool:
        """ Inserts an element at the end of the circular queue. Return true if the operation is successful.

        Args:
            value: The value to be added to the queue

        Returns:
            A boolean to indicate success
        """
        # is there room?
        if self.currentSize == self.capacity:
            return False # no room at the inn

        # special case for first element
        if self.frontPointer == None:
            self.frontPointer = 0
            self.rearPointer = 0
        else:            
            # New items are added to the end
            self.rearPointer += 1

            # did it wrap around?
            if self.rearPointer == self.capacity:
                self.rearPointer = 0

        # add the item
        self.circularQueue[self.rearPointer] = value
        self.currentSize += 1
        return True

    def deQueue(self) -> bool:
        """ Deletes the element at the front of the circular queue.

        Returns:
            A boolean to indicate success
        """
        if self.currentSize == 0:
            return False
        
        # if there is only element we become empty
        if self.frontPointer == self.rearPointer:
            self.frontPointer = self.rearPointer = None
        else:
            # remove from the front by increasing the pointer
            self.frontPointer += 1

            # did it wrap around?
            if self.frontPointer == self.capacity:
                self.frontPointer = 0

        self.currentSize -= 1
        return True


    def Front(self) -> int:        
        """ Gets the front item from the queue

        Returns:
            The front item.
            -1 indicates an empty queue.
        """
        if self.currentSize != 0:
            return self.circularQueue[self.frontPointer]
        else:
            return -1


    def Rear(self) -> int:
        """ Gets the last item from the queue.

        Returns:
            The last item.
            -1 indicates an empty queue.
        """
        if self.currentSize != 0:
            return self.circularQueue[self.rearPointer]
        else:
            return -1
        
    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty or not.

        Returns:
            A boolean to indicate if the queue is empty.
        """
        return self.currentSize == 0

    def isFull(self) -> bool:
        """Checks whether the circular queue is full or not.

        Returns:
            A boolean to indicate if the queue is full.
        """
        return self.currentSize == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

mcq = MyCircularQueue(3)

print(mcq.isEmpty())  # return True
print(mcq.Rear())     # return -1
print(mcq.Front())    # return -1
print(mcq.isFull())   # return False

print(mcq.enQueue(1)) # return True
print(mcq.enQueue(2)) # return True
print(mcq.enQueue(3)) # return True
print(mcq.enQueue(4)) # return False
print(mcq.Rear())     # return 3
print(mcq.isFull())   # return True
print(mcq.deQueue())  # return True
print(mcq.enQueue(4)) # return True
print(mcq.Rear())     # return 4

print(mcq.deQueue())  # return True
print(mcq.deQueue())  # return True
print(mcq.deQueue())  # return True
print(mcq.deQueue())  # return False