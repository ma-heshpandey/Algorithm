'''
Stack can be list as well,like list.append() and list.pop() but due to memory allo
cation, list will be transfered to new place if memory grt filled so it is expensive  
thus collections library implements by doubly link for easy implementation

'''

from collections import deque

class Stack:
    
    def __init__(self):
        self.container=deque()
        
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        self.container.pop()
        
    def peak(self):
        return self.container[-1]
    
    def size(self):
        return len(Self.container)
    
    
s=Stack()
s.push(1)
s.push(2)
s.pop()
print(s.peak())    