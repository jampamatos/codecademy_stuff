class Node
	attr_accessor :value, :prev_node, :next_node
	
	def initialize(value, prev_node=nil, next_node = nil)
	  @value = value
	  @prev_node = prev_node
	  @next_node = next_node
	end
end