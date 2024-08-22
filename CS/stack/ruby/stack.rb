require_relative 'node'

class Stack
    def initialize(limit = 1000)
        @limit = limit
        @top_item = nil
        @size = 0
    end

    def push(value)
        raise 'Stack overflow' unless has_space?

        new_node = Node.new(value)
        new_node.next_node = @top_item
        @top_item = new_node
        @size += 1
    end

    def pop
        raise 'Stack is empty' if empty?

        node_to_remove = @top_item
        @top_item = node_to_remove.next_node
        @size -= 1

        node_to_remove.value
    end

    def peek
        raise 'Stack is empty' if empty?

        @top_item.value
    end

    def has_space?
        @limit > @size
    end

    def empty?
        @size == 0
    end
end