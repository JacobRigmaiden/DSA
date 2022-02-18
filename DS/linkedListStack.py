
class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.empty():
            return None
        else:
            nodeToRemove = self.head
            self.head = nodeToRemove.next
            nodeToRemove.next = None
            return nodeToRemove.data
    
    def size(self):
        if self.head == None:
            return 0    
        counter = 0
        node = self.head 
        while node:
            counter += 1
            node = node.next
        return counter

    def top(self):
        return self.head.data
    
    def empty(self):
        return self.head == None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None