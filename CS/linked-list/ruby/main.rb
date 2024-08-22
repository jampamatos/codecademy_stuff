require_relative 'linked_list'
require_relative 'doubly_list'

ll = LinkedList.new
ll.insert_beginning(1)
ll.insert_beginning(2)
ll.insert_beginning(3)
ll.insert_beginning(4)
puts "Lista Original:"
puts ll.stringify_list

ll.swap_node(3, 1)
puts "Lista Após Trocar 3 e 1:"
puts ll.stringify_list

ll.swap_node(2, 4)
puts "Lista Após Trocar 2 e 4:"
puts ll.stringify_list

ll.swap_node(4, 4)
puts "Tentativa de Trocar 4 e 4 (não deve ocorrer troca):"
puts ll.stringify_list

ll.swap_node(5, 6)
puts "Tentativa de Trocar 5 e 6 (não presentes na lista):"
puts ll.stringify_list  