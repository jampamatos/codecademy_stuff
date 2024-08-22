from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
    
    def find_node(self, val):
        node_prev = None
        node = self.head_node

        while node is not None:
            if node.get_value() == val:
                break
            node_prev = node
            node = node.get_next_node()
        
        return node_prev, node
    
    def swap_node(self, val1, val2):
        print(f"Swapping {val1} with {val2}")

        if val1 == val2: 
            print(f'Elements are the same - no swap needed')
            return

        node1_prev, node1 = self.find_node(val1)
        node2_prev, node2 = self.find_node(val2)

        if (node1 is None or node2 is None):
            print("Swap not possible - one or more element is not in the list")
            return
        
        if node1_prev is None: 
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)
        
        if node2_prev is None: 
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)