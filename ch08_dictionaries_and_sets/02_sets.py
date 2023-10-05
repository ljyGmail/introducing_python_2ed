# @ Sets

# @@ Create with set()
empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

# @@ Convert with set()
# make a set from a string
print(set('letters'))
# make a set from a list
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
# make a set from a tuple
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
# make a set from a dictionary (only keys are used)
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

# @@ Get Length with len()
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))

# @@ Add an item with add()
s = set((1, 2, 3))
print(s)
s.add(4)
print(s)

# @@ Delete an Item with remove()
s = set((1, 2, 3))
s.remove(3)
print(s)

# @@ Iterate with for and in
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

print('#' * 20)

# @@ Test for a Value with in
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print('#' * 20)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

print('#' * 20)

# @@ Combinations and Operators
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print('#' * 20)

# rewrite the previous code using set intersection operator (&)
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

print('#' * 20)

a = {1, 2}
b = {2, 3}

# intersection
print(a & b)
print(a.intersection(b))

print(bruss & wruss)

# union
print(a | b)
print(a.union(b))

print(bruss | wruss)

# difference
print(a - b)
print(a.difference(b))

print(bruss - wruss)
print(wruss - bruss)

# exclusive
print(a ^ b)
print(a.symmetric_difference(b))

print(bruss ^ wruss)

# subset
print(a <= b)
print(a.issubset(b))

print(bruss <= wruss)

print(a <= a)
print(a.issubset(a))

# proper subset
print(a < b)
print(a < a)

print(bruss < wruss)

# superset
print(a >= b)
print(a.issuperset(b))

print(wruss >= bruss)

print(a >= a)
print(a.issuperset(a))

# proper superset
print(a > b)

print(wruss > bruss)

print(a > a)

# @@ Set Comprehensions
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

# @@ Create an Immutable Set with frozenset()
print(frozenset([3, 2, 1]))
print(frozenset(set([2, 1, 3])))
print(frozenset({3, 1, 2}))
print(frozenset((2, 3, 1)))

print('#' * 20)
# Is it really frozen?
fs = frozenset([3, 2, 1])
print(fs)
# fs.add(4)
