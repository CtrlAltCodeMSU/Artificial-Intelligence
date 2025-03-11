from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack Elements: " , list(self.stack))
s = Stack()
s.push(20)
s.push(30)

print("Top element:", s.peek())  
print("Popped element:", s.pop())
print("Stack size:", s.size())  

s.display()
        