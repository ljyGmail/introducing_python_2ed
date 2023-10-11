# @ Tuples

# @@ Create with Commas and ()
empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

one_marx = ('Groucho',)
print(one_marx)

one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

one_marx = 'Groucho',
print(type(one_marx))

print(type('Groucho',))
print(type(('Groucho',)))

# Tuples let you assign multiple variables at once:
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple  # tuple unpacking
print(a)
print(b)
print(c)

# use tuples to exchange values in one statement without using a temporary variable:
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)

# @@ Create with tuple()
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

# @@ Combine Tuples by Using +
print(('Groucho',)+('Chico', 'Harpo'))

# @@ Duplicate Items with *
print(('yada',) * 3)

# @@ Compare Tuples
a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a < b)

# @@ Iterate with for and in
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

# @@ Modify a Tuple
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(t1 + t2)

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
t1 += t2
print(t1)

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))
t1 += t2
print(id(t1))
