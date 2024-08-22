from node import Node

class Queue:
    
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size
    
    def enqueue(self, value):
        if not self.has_space(): raise Exception('No more room.')
        
        new_node = Node(value)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.is_empty(): raise Exception('Queue is empty.')
        
        node_to_remove = self.head
        
        if self.size == 1: self.head = self.tail = None
        else: self.head = node_to_remove.get_next_node()
        
        self.size -= 1
        return node_to_remove.get_value()
    
    def peek(self):
        if self.is_empty(): return None
        
        return self.head.get_value()
    
    def get_size(self):
        return self.size
    
    def has_space(self):
        return not self.max_size or self.max_size > self.size

    def is_empty(self):
        return self.size == 0