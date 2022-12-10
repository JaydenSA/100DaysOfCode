numbers = input('Please enter a set of numbers: \n').split()
# debugging print(numbers)

sum = 0
count = 0
for num in numbers: 
    sum += int(num)
    count += 1

average = sum / count
print(str(average))