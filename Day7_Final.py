import Day7_Hangman_Art
import Day7_Hangman_Words
import random 

#initiasing all variables 
chosen_word = random.choice(Day7_Hangman_Words.word_list)
end_of_game = False 

# game functional variables 
guessed = False
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# displaying logo
print(Day7_Hangman_Art.logo)

#Create blanks
display = []
for i in range(0, len(chosen_word)):
  display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print('You have already tried this word, please try again. ')
        continue
    
    #Check guessed letter
    for number in range(len(chosen_word)):
        letter = chosen_word[number]
        if letter == guess:
            display[number] = guess
            guessed = True 

    if guessed == False: 
        print('The letter you have entered ' + guess + ' is not in the word. Please try again')
        lives -= 1
        if lives < 1:
            print('You lost!')
            end_of_game = True
    
    print(Day7_Hangman_Art.stages[lives])
    word = ''
    for letter in display:
        word += letter
    print('Word: ' + word)

    if '_' not in display:
        print('You won!')
        end_of_game = True

    # clearing variables 
    guessed = False