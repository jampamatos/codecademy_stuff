require_relative 'node'

class LinkedList
	def initialize(value = nil)
	  @head_node = Node.new(value)
	end
  
	def get_head_node
	  @head_node
	end
  
	def insert_beginning(new_value)
	  new_node = Node.new(new_value, @head_node)
	  @head_node = new_node
	end
  
	def stringify_list
	  string_list = ''
	  current_node = @head_node
	  while current_node
		string_list << current_node.value.to_s + "\n" if current_node.value
		current_node = current_node.next_node
	  end
	  string_list
	end
  
	def remove_node(value_to_remove)
	  current_node = @head_node
  
	  if current_node && current_node.value == value_to_remove
		@head_node = current_node.next_node
		return
	  end
  
	  while current_node
		next_node = current_node.next_node
		if next_node && next_node.value == value_to_remove
		  current_node.next_node = next_node.next_node
		  break
		else
		  current_node = next_node
		end
	  end
	end
  
	def find_node(val)
	  node_prev = nil
	  node = @head_node
  
	  while node
		break if node.value == val
		node_prev = node
		node = node.next_node
	  end
  
	  [node_prev, node]
	end
  
	def swap_node(val1, val2)
	  puts "Swapping #{val1} with #{val2}"
  
	  if val1 == val2
		puts 'Elements are the same - no swap needed'
		return
	  end
  
	  node1_prev, node1 = find_node(val1)
	  node2_prev, node2 = find_node(val2)
  
	  if node1.nil? || node2.nil?
		puts "Swap not possible - one or more element is not in the list"
		return
	  end
  
	  node1_prev.nil? ? @head_node = node2 : node1_prev.next_node = node2
	  node2_prev.nil? ? @head_node = node1 : node2_prev.next_node = node1
  
	  
	  temp = node1.next_node
	  node1.next_node = node2.next_node
	  node2.next_node = temp
	end
end