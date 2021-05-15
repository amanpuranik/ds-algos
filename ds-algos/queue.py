from collections import deque



class Queue:

    def __init__(self):
        self.buffer = deque

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def size(self):
        return len(self.buffer)


q = Queue()

q.enqueue(1)
q.enqueue(2)


#implementation as a list

q = []

q.append(1)
q.append(2)

print(q)

q.pop()

print(q)
