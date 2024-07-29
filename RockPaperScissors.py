import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


user_choice = int(input("what do you choose, 0 for rock, 1 for paper, 2 for scissors\n "))
choices = [rock, paper, scissors]

if user_choice > len(choices):
    print("invalid input, you lose")
else:
    print(f"you chose: {choices[user_choice]} \n")

    computer_choice = random.randint(0, 2)
    print(f"computer chose \n {choices[computer_choice]}")

    if user_choice >= 3 or user_choice < 0:
        print("invalid input, You lose")
    elif computer_choice == 0 and user_choice == 2:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("draw")
