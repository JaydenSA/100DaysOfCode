# building calculator

def add(n1, n2): return n1 + n2
def sub(n1, n2): return n1 - n2
def mul(n1, n2): return n1 * n2
def div(n1, n2): return n1 / n2

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def calculations(num1, num2, symbol):
    calculationfunction = operators[symbol]
    final_answer = calculationfunction(num1,num2)
    print(f'{num1} {symbol} {num2} = {final_answer}')
    return final_answer

on = True
while on: 
    num1 = int(input('Please enter the first number you would like to work with: '))
    for operator in operators:
        print(operator)
    symbol = input('Please select one of the above by typing it: ')
    num2 = int(input('Please enter the second number you would like to work with: '))

    saved_answer = calculations(num1, num2, symbol)
    continued = input('Would you like to keep adding to this? Y/N').lower()
    if continued == 'y':
        for operator in operators:
            print(operator)
        symbol = input('Please select one of the above by typing it: ')
        num2 = int(input('Please enter the second number you would like to work with: '))
        another_saved_answer = calculations(saved_answer, num2, symbol)
    else: 
        on = False
