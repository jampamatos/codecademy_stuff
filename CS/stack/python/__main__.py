from stack import Stack, Hanoi

print("Let's play Towers of Hanoi!!\n")

# Create the stacks
stacks = [Hanoi('Left'), Hanoi('Middle'), Hanoi('Right')]

# Set up the Game
num_disks = int(input("How many disks do you wish to play with?\n"))
while num_disks < 3:
  num_disks = int(input('Enter a number greater than or equal to 3\n'))

for i in range(num_disks, 0, -1): stacks[0].push(i)

optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {optimal_moves} moves!")

# Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  
  while True:
    for letter, stack in zip(choices, stacks): print(f"Enter {letter} for {stack.get_name()}")
    
    user_input = input('').upper()
    
    if user_input in choices: return stacks[choices.index(user_input)]

# Play the Game
num_user_moves = 0

while (stacks[-1].get_size() != num_disks):
  print("\n\n\n...Current Stacks...")
  for stack in stacks: stack.print_items()

  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if not from_stack: 
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
  
  print(F"\n\nYou completed the game in {num_user_moves}, and the optimal number of moves is {optimal_moves}")