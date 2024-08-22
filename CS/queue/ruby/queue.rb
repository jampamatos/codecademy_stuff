require_relative 'node'

class Queue
    attr_reader :size

    def initialize(max_size = nil)
        @head = nil
        @tail = nil
        @size = 0
        @max_size = max_size
    end

    def enqueue(value)
        raise 'No more room.' unless has_space?

        new_node = Node.new(value)

        if empty?
            @head = @tail = new_node
        else
            @tail.next_node = new_node
            @tail = new_node
        end

        @size += 1
    end

    def dequeue
        raise 'Queue is empty.' if empty?

        node_to_remove = @head
        @head = @head.next_node

        @tail = nil if @head.nil?
        @size -= 1

        node_to_remove.value
    end

    def peek
        empty? ? nil : @head.value
    end

    def has_space?
        @max_size.nil? || @max_size > @size
    end

    def empty?
        @size == 0
    end
end
