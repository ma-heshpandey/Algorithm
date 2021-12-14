
'''
Using concept of inheritance

'''


from collections import deque


class Queue(deque):
    
    def __init__(self):
        super(deque,self).__init__()
        
    def enqueue(self,val):
        super().appendleft(val)
        
    def dequeue(self):
        return super().pop()
    
    def is_empty(self):
        length=len(self)
        if length==0:
            return True
        else:
            return False
    
q=Queue()
q.enqueue(23)
q.enqueue(24)
q.dequeue()
print(q.dequeue())
print(q.is_empty())
