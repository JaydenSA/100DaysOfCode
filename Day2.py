print('Welcome to the tip calculator.')
total_bill = input('What is the total bill? $')
total_people = input('How many people to split the bill? ')
percentage_tip = input('What percentage tip would you like to give? 10, 12, 15? ')

per_person = int(total_bill) / int(total_people)
per_person += int(per_person) / int(percentage_tip)

print('Each person should pay: $' + str(per_person))