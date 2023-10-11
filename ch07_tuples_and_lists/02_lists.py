# @ Lists

# @@ Create with []
import copy
empty_list = []
print(empty_list)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekdays)
big_birds = ['emu', 'ostrich', 'cassowary']
print(big_birds)
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
print(first_names)
leap_years = [2000, 2004, 2008]
print(leap_years)
randomness = ['Punxsatawney', {"groundhog": "Phil"}, "Feb. 2"]
print(randomness)
print('#' * 20)

# @@ Create with list()
another_empty_list = list()
print(another_empty_list)

print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# @@ Create from a String with split()
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))

# more than one separator string in a row
splitme = 'a/b//c/d///e'
print(splitme.split('/'))

# use two-character separator string //
splitme = 'a/b//c/d///e'
print(splitme.split('//'))
print('#' * 20)

# @@ Get an Item by [offset]
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])

# negative indexes
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

# IndexError
# print(marxes[5])
# print(marxes[-5])
print('#' * 20)

# @@ Get Items with a Slice
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])

# step by 2
print(marxes[::2])

# start at the end, step by 2
print(marxes[::-2])

# reverse a list
print(marxes[::-1])

# To reverse a list in place:
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.reverse()
print(marxes)

# an invalid index in slicing does not cause an exception
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])
print('#' * 20)

# @@ Add an Item to te End with append()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)
print('#' * 20)

# @@ Add an Item by Offset with insert()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')  # no exception
print(marxes)
print('#' * 20)

# @@ Duplicate All Items with *
print(['blah'] * 3)
print('#' * 20)

# @@ Combine Lists by Using extend() or +
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

# if we had append(), others would have been added as single list item
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)
print('#' * 20)

# @@ Change an Item by [offset]
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)
print('#' * 20)

# @@ Change Items with a Slice
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)

# the number of elements doesn't need to be the same
numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)

# the righthand thing doesn't even need to e a list:
numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers)
print('#' * 20)

# @@ Delete an Item by Offset with del
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])
del marxes[-1]
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes)
print('#' * 20)

# @@ Delete an Item by Value with remove()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)
print('#' * 20)

# @@ Get an Item by Offset and Delete It with pop()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)
print('#' * 20)

# @@ Delete All Items with clear()
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)
print('#' * 20)

# @@ Find an Item's Offset by Value with index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))
print('#' * 20)

# @@ Test for a Value with in
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)

words = ['a', 'deer', 'a', 'female', 'deer']
print('deer' in words)
print('#' * 20)

# @@ Count Occurrences of a Value with count()
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))
print('#' * 20)

# @@ Convert a List to a String with join()
marxes = ['Groucho', 'Chico', 'Harpo']
print(','.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)
print('#' * 20)

# @@ Reorder Items with sort() or sorted()
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)

marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)
print('#' * 20)

# @@ Get Length with len()
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))
print('#' * 20)

# @@ Assign with =
a = [1, 2,  3]
print(a)
b = a
print(b)

a[0] = 'surprise'
print(a)
print(b)

b[0] = 'I hate surprises'
print(b)
print(a)
print('#' * 20)

# @@ Copy with copy(), list() or a Slice
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)
print('#' * 20)

# @@ Copy Everything with deepcopy()
a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]

print(a)
print(b)
print(c)
print(d)

a[2][1] = 10
print(a)
print(b)
print(c)
print(d)
print('#' * 20)

a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)

a[2][1] = 10
print(a)
print(b)

print('#' * 20)

# @@ Compare Lists
a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a < b)

print('#' * 20)

# @@ Iterate with for and in
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)
print()


cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
print()

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x'")
print()

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # no break means no cheese
    print('This is not much of a cheese shop, is it?')

print('#' * 20)

# @@ Iterate Multiple Sequences with zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ': drink', drink, '- eat', fruit, '- enjoy', dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list(zip(english, french)))

print(dict(zip(english, french)))

print('#' * 20)

# @@ Create a List with a Comprehension
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)

print(number_list)

number_list = list(range(1, 6))
print(number_list)

number_list = [number for number in range(1, 6)]
print(number_list)

number_list = [number - 1 for number in range(1, 6)]
print(number_list)

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)

# traditional counterpart:
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)

print(a_list)

rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

print('#' * 20)

# @@ Lists of Lists
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])
