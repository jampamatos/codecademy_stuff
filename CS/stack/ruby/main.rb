require_relative 'stack'

puts "Lat's play Towers of Hanoi!!\n\n"

# Create the stacks
stacks = [Hanoi.new('Left'), Hanoi.new('Middle'), Hanoi.new('Right')]

# Set up the Game
puts 'How many disks do you wish to play with?'
num_disks = gets.chomp.to_i

while num_disks < 3
    puts 'Enter a number greater than or equal to 3'
    num_disks = gets.chomp.to_i
end

num_disks.downto(1) { |i| stacks[0].push(i) }

optimal_moves = 2**num_disks - 1
puts "\nThe fastest you can solve this game is in #{optimal_moves} moves!"

# Get User Input
def get_input(stacks)
    choices = stacks.map { |stack| stack.name[0].upcase }

    loop do
        choices.zip(stacks).each { |letter, stack| puts "Enter #{letter} for #{stack.name}" }

        user_input = gets.chomp.upcase
        return stacks[choices.index(user_input)] if choices.include?(user_input)
    end
end

# Play the Game