from linked_list import LinkedList
from doubly_list import DoublyLinkedList

ll = LinkedList()
ll.insert_beginning(1)
ll.insert_beginning(2)
ll.insert_beginning(3)
ll.insert_beginning(4)
print("Lista Original:")
print(ll.stringify_list())

ll.swap_node(3, 1)
print("Lista Após Trocar 3 e 1:")
print(ll.stringify_list())

ll.swap_node(2, 4)
print("Lista Após Trocar 2 e 4:")
print(ll.stringify_list())

ll.swap_node(4, 4)
print("Tentativa de Trocar 4 e 4 (não deve ocorrer troca):")
print(ll.stringify_list())

ll.swap_node(5, 6)
print("Tentativa de Trocar 5 e 6 (não presentes na lista):")
print(ll.stringify_list())