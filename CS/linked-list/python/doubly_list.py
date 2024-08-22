from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    
    def get_head_node(self):
        return self.head_node
  
    def set_head_node(self, new_node):
        self.head_node = new_node

    def get_tail_node(self):
        return self.tail_node
    
    def set_tail_node(self, new_node):
        self.tail_node = new_node

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.get_head_node()

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        
        self.set_head_node(new_head)

        if self.get_tail_node() is None: self.set_tail_node(new_head)
    
    def remove_head(self):
        removed_head = self.head_node
        if removed_head is None: return None

        self.head_node = removed_head.get_next_node()
        if self.head_node is not None: self.head_node.set_prev_node(None)

        if removed_head == self.tail_node: self.remove_tail()

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node
        if removed_tail is None: return None

        self.tail_node = removed_tail.get_prev_node()
        if self.tail_node is not None: self.tail_node.set_next_node(None)

        if removed_tail == self.head_node: self.remove_head()

        return removed_tail.get_value()