

class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def top(self):
        return self.items[0]
    
    def pop(self):
        self.items.pop(0)
    
    def size(self):
        return len(self.items)

    def empty(self):
        return self.items == []

