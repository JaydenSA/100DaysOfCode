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

#Write your code below this line 👇
import random
images = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors.\n'))
computer_choice = random.randint(0,2)
# debugging print(str(computer_choice))

if user_choice >= 3 or user_choice < 0: 
    print('You have entered an invalid response, please try again. ')
    exit()
else:
    print('My Choice: \n')
    print(images[computer_choice])
    print('Your Choice: \n')
    print(images[user_choice])

    if user_choice == 0 and computer_choice == 2:
        print('You win! You choose rock and I choose scissors.\n')
    elif user_choice == 1 and computer_choice < 1:
        print('You win! You choose paper and I choose rock. \n')
    elif user_choice == 2 and computer_choice == 1:
        print('You won! You choose scissors and I choose paper.\n')
    elif user_choice == computer_choice:
        print('Draw!')
    else:
        if user_choice == 0:
            print('You lose! You choose rock and I choose paper.\n')
        elif user_choice == 1:
            print('You lose! You choose paper and I choose scissors. \n')
        elif user_choice == 2:
            print('You lose! You choose scissors and I choose rock.\n')
