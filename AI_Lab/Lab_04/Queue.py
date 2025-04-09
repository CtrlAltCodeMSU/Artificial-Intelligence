class Queue:
    def __init__(self, arr , size):
        self.arr = arr
        self.size = size
        self.front = 0
        self.rear = -1
        
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        else:
            self.rear += 1
            self.arr.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            item = self.arr[self.front]
            self.arr.pop(0)
            self.rear -=1
            return item
    def is_empty(self):
        return self.rear < 0
    def is_full(self):
        return self.rear >= self.size-1
    def display(self):
        print("Queue: ", self.arr)
        
        
array = []
q = Queue(array , 7)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
# q.enqueue(60)
# q.enqueue(70)
q.dequeue()
q.dequeue()
q.display()

q.enqueue(70)
