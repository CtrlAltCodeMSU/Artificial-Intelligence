class Stack:
    def __init__(self, arr , size):
        self.arr = arr 
        self.size = size
        self.top = -1
    def push(self, value):
        if not self.isFull():
            self.top += 1
            self.arr.append(value)
    def pop(self):
        if not self.isEmpty():
            self.arr.pop()
            self.top -= 1
        else:
            print("Stack is Empty")
    def isEmpty(self):
        return self.top< 0
    def isFull(self):
        return (self.top >= self.size-1)
    def peek(self):
        return self.arr[self.top]
    def display(self):
        print(self.arr)
    
arr = []
s = Stack(arr, 100)

for i in range(5):
    s.push(i)
    

print("Peek Element: " , s.peek())
s.display()
        
        
            
            