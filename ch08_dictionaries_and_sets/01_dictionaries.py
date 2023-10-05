import copy
# @ Dictionaries

# @@ Create with {}
empty_dict = {}
print(empty_dict)

bierce = {
    'day': 'A period of twenty-four hours, mostly misspent',
    'positive': "Mistaken at the top of one's voice",
    'misfortune': 'The kind of fortune that never misses',
}
print(bierce)

# @@ Create with dict()
# The traditional way:
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)

# Using dict():
acme_customer = dict(first='Wile', middle='E', last='Coyote')
print(acme_customer)

# One limitation of the second way is that the argument names need to be legal variable names.
# x=dict(name='Elmer', def='hunter')

# @@ Convert with dict()
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

# A list of two-item tuples:
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))

# A tuple of two-item lists:
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

# A list of two-character strings:
los = ['ab', 'cd', 'ef']
print(dict(los))

# tuple of two-character strings:
tos = ('ab', 'cd', 'ef')
print(dict(tos))

# @@ Add or Change an Item by [key]
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
print(some_pythons)

# @@ Get an Item by [key] or with get()
print(some_pythons['John'])

# some_pythons['Groucho']

print('Groucho' in some_pythons)
print(some_pythons.get('John'))
print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))

# @@ Get All Keys with keys()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
print(list(signals.keys()))

# @@ Get All Values with values()
print(list(signals.values()))

# @@ Get Key-Value Pairs with items()
print(list(signals.items()))

# @@ Get Length with len()
print(len(signals))

# @@ Combine Dictionaries with {**a, **b}
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})

# pass more than two dictionaries
third = {'d': 'donuts'}
print({**first, **second, **third})

# @@ Combine Dictionaries with update()
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)

# @@ Delete an Item by Key with del
del pythons['Marx']
print(pythons)

del pythons['Howard']
print(pythons)

# @@ Get an Item by Key and Delete It with pop()
print(len(pythons))

print(pythons.pop('Palin'))

print(len(pythons))

# print(pythons.pop('Palin'))
print(pythons.pop('First', 'Hugo'))
print(len(pythons))

# @@ Delete All Items with clear()
pythons.clear()
print(pythons)

pythons = {}
print(pythons)

# @@ Test for a Key with in
pythons = {'Chapman': 'Graham', 'Cleese': 'John',
           'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

# @@ Assign with =
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

# @@ Copy with copy()
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

# @@ Copy Everything with deepcopy()
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': ['stop', 'smile']}
signals_copy = signals.copy()
print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

# deep copy
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': ['stop', 'smile']}

signals_copy = copy.deepcopy(signals)

print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

# @@ Compare Dictionaries
a = {1: 1, 2: 2, 3: 3}
b = {3: 3, 1: 1, 2: 2}
print(a == b)

# Other operators won't work:
# print(a <= b)

a = {1: [1, 2], 2: [1], 3: [1]}
b = {1: [1, 1], 2: [1], 3: [1]}
print(a == b)

# @@ Iterate with for and in
accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}

for card in accusation:  # or, for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# @@ Dictionary Comprehensions
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter)
                for letter in set(word) if letter in vowels}
print(vowel_counts)
