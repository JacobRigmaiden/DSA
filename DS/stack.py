# Implement a Stack

# Functionality Overview
# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

class Stack:
    def __init__(self):
        self.items = []
    
    def empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

