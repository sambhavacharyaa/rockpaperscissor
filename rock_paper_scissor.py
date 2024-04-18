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

user_choice = int(input("Types 0 for Rock, 1 for Paper and 2 for scissors"))
print("You chose: \n")
game_images = [rock, paper, scissors]
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose: \n")

print(game_images[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("Invalid choice")
elif user_choice == 0 and computer_choice == 2:
    print("You won")
elif computer_choice == 0 and user_choice ==2:
    print("You lost")
elif user_choice == 1 and computer_choice == 0:
    print("You won")
elif user_choice == 0 and computer_choice == 1:
    print("You lost")
elif user_choice == 2 and computer_choice == 1:
    print("You won")
elif user_choice == 1 and computer_choice == 2:
    print("You lost")
else:
    print("You tied")