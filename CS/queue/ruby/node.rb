class Node
    attr_reader :value
    attr_accessor :prev_node, :next_node

    def initialize(value, prev_node = nil, next_node = nil)
        @value = value
        @prev_node = prev_node
        @next_node = next_node
    end
end