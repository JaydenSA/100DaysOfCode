print("Welcome to the BMI Calculator. ")
height = input("Please enter your height in meters: ")
weight = input("Please enter your weight in kilograms: ")

bmi = round(int(weight) / (float(height) * 2))

if bmi > 35: 
    print('Your BMI is ' + str(bmi) + '. You are clinically obese.')
    exit()
elif bmi > 30:
    print('Your BMI is ' + str(bmi) + '. You are obese.')
    exit()
elif bmi > 25:
    print('Your BMI is ' + str(bmi) + '. You are overweight.')
    exit()
elif bmi > 18.5:
    print('Your BMI is ' + str(bmi) + '. You are normal weight.')
    exit()
else:
    print('Your BMI is ' + str(bmi) + '. You are underweight.')