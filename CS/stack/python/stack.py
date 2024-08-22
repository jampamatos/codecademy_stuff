from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.limit = limit
        self.top_item = None
        self.size = 0
    
    def push(self, value):
        if not self.has_space(): raise Exception('Stack Overflow')
        
        new_node = Node(value)
        new_node.set_next_node(self.top_item)
        self.top_item = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty(): raise Exception('Stack is empty')
        
        node_to_remove = self.top_item
        self.top_item = node_to_remove.get_next_node()
        self.size -= 1
        
        return node_to_remove.get_value()
    
    def peek(self):
        if self.is_empty(): raise Exception('Stack is empty')
        
        return self.top_item.get_value()
    
    def has_space(self):
        return self.limit > self.size
    
    def is_empty(self):
        return self.size == 0