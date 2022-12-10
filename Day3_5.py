print('Welcome to the Love Calculator')
name1 = input('What is your name? ').lower()
name2 = input('What is their name? ').lower()

count_true = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
count_true += name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')

count_love = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')
count_love += name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

total = str(count_true) + str(count_love)

if int(total) > 90 or int(total) < 10:
    print('Your match is '+ str(count_true)+str(count_love) + ', you go together like  coke and mentos')
elif int(total) > 39 and int(total) < 51:
    print('Your match is '+ str(count_true)+str(count_love) + ', you are alright together.')
else:
    print('Your match is '+ str(count_true)+str(count_love))