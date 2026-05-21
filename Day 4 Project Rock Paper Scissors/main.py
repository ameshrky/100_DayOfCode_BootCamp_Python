import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options: list[str] = [rock, paper, scissors]


player_selection_idx = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_selection_idx >= 3 or player_selection_idx < 0:
    print("You typed an invalid number. You lose!")
else:
        print(options[player_selection_idx])
        computer_choice_idx = random.randint(0,2)
        print("Computer chose:\n")
        print(options[computer_choice_idx])
        if player_selection_idx == computer_choice_idx:
            print("It's a draw")
        elif (player_selection_idx == 0 and computer_choice_idx == 2) \
            or (player_selection_idx == 1 and computer_choice_idx == 0)\
            or (player_selection_idx == 2 and computer_choice_idx == 1):
            print("You win!")
        else:
            print("You lose!")
