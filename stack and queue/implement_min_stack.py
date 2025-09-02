from collections import deque
import sys
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = sys.maxsize

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min =val
        else:
            if val<self.min:
                self.stack.append(2*val-self.min)
                self.min=val
            else:
                self.stack.append(val)
    def pop(self):
        if not self.stack:
            return 
        x = self.stack.pop()
        if x<self.min:
            current_min = self.min
            self.min = (2*self.min)-x
            return current_min
        return x

    def top(self):
        if not self.stack:
            return 
        if self.stack[-1]<self.min:
            return self.min
        return self.stack[-1]
    def getMin(self):
        return self.min
    
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(3)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())

print(minStack.getMin())