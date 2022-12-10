print('Welcome to Python Pizza Deliveries')

size = input('What size pizza would you like? S, M, L :')
add_pep = input('Would you want pepperoni? Y or N: ')
extra_cheese = input('Would you like extra cheese? Y or N: ')

bill = 0

if size == 'S':
    bill = 15
    if add_pep == 'Y':
        bill += 2
elif size == 'M':
    bill = 20 
    if add_pep == 'Y':
        bill += 3
elif size == 'L':
    bill = 25
    if add_pep == 'Y':
        bill += 3

if extra_cheese == 'Y':
    bill += 1 

print('Your bill is: $' + str(bill))