class DoublyLinkedList
    attr_accessor :head_node, :tail_node

    def initialize
        @head_node = nil
        @tail_node = nil
    end

    def add_to_head(new_value)
        new_head = Node.new(new_value)
        current_head = @head_node

        if current_head
            current_head.prev_node = new_head
            new_head.next_node = current_head
        end

        @head_node = new_head
        @tail_node = new_head unless @tail_node
    end

    def add_to_tail(new_value)
        new_tail = Node.new(new_value)
        current_tail = @tail_node

        if current_tail
            current_tail.next_node = new_tail
            new_tail.prev_node = current_tail
        end

        @tail_node = new_tail
        @head_node = new_tail unless @head_node
    end

    def remove_head
        removed_head = @head_node
        return nil unless removed_head

        @head_node = removed_head.next_node
        @head_node ? @head_node.prev_node = nil : @tail_node = nil
        
        removed_head.value
    end

    def remove_tail
        removed_tail = @tail_node
        return nil unless removed_tail

        @tail_node = removed_tail.prev_node
        @tail_node ? @tail_node.next_node = nil : @head_node = nil

        removed_tail.value
    end
end