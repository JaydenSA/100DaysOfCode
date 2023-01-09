# pre processors 
import random
import Day11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#dealing two cards to user and computer 
hand_computer = []
hand_user = []
def dealer():
    return cards[random.randint(0, 12)]
def card(): 
    for i in range(2):
        hand_computer = []
        hand_user = []
        hand_computer.append(dealer())
        hand_user.append(dealer())
card()
total_computer = sum(hand_computer)
total_user = sum(hand_user)

#checking the status of the game, looking for wins 
def check_status(list):
    if sum(list) == 21 and len(list) == 2:
        return 'blackjack'

#printing totals and cards 
def printing_totals():
    print(f'The computers hand is: {hand_computer[0]}')
    print(f'Your hand is: {hand_user}, total sum is {total_user}')

#printing logo 
print(Day11.logo)

#game loop
gameplay = True
while(gameplay):
    game = input('Would you like to play a game of blackjack? Type Y or N: ').lower()
    if game == 'y':
        card()
        printing_totals()
    else:
        break

    if check_status(hand_computer) == 'blackjack':
        print('Computer got blackjack! You lose!')

    
    another = True
    while another:
        another_card = input('Would you like another card? Type Y or N: ').lower()
        if another_card == 'y':
            hand_user.append(dealer())
            total_user = sum(hand_user)
            printing_totals()
            if total_user > 21: 
                print('You lose! Your total went over 21!')
                another = False
        elif another_card == 'n':
            another = False
