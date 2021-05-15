#use collections deque for stacks in python

from collections import deque


stack = deque()



class Stack:

    def __init__(self):
        self.container = deque()


    def push(self,val):
        self.container.append(val)


    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]



s = Stack()

s.push(5)
s.push(6)
s.push(7)
s.push(8)

print(s.container)
s.pop()
print(s.peek())