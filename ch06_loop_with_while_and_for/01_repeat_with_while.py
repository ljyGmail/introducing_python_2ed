# @ Repeat with while
count = 1
while count <= 5:
    print(count)
    count += 1

# @@ Cancel with break
while True:
    stuff = input('String to capitalize [type q to quit]: ')
    if stuff == 'q':
        break
    print(stuff.capitalize())

# @@ Skip Ahead with continue
while True:
    value = input('Integer, please [q to quit]: ')
    if value == 'q':  # quit
        break
    number = int(value)  # an even number
    if number % 2 == 0:
        continue
    print(number, 'squared is', number*number)

# @@ Check break Use with else
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:  # break not called
    print('No even number found')
