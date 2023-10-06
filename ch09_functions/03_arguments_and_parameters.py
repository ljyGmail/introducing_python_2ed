# @ Arguments and Parameters

def echo(anything):
    return anything+' ' + anything


print(echo('Rumplestiltskin'))


def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


comment = commentary('blue')
print(comment)


def do_nothing():
    pass


# If a function doesn't call return explicitly, the caller gets the result None.
print(do_nothing())

# @@ None Is Useful
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

thing = None
if thing is None:
    print("It's nothing")
else:
    print("It's something")


def whatis(thing):
    if thing is None:
        print(thing, 'is None')
    elif thing:
        print(thing, 'is True')
    else:
        print(thing, 'is False')


whatis(None)
whatis(True)
whatis(False)

whatis(0)
whatis(0.0)
whatis('')
whatis("")
whatis('''''')
whatis(())
whatis([])
whatis({})
whatis(set())

whatis(0.00001)
whatis([0])
whatis([''])
whatis(' ')

# @@ Positional Arguments


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))

# downside of positional arguments is to remember the meaning of each position.
print(menu('beef', 'bagel', 'bordeaux'))


# @@ Keyword Arguments
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# mix position and keyword arguments
menu('frontenac', dessert='flan', entree='fish')

# @@ Specify Default Parameter Values


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))

# Default parameter values are calculated when the function is defined, not when it is run.


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')  # expect ['b']

# It would have worked if it had been written like this:


def works(arg):
    result = []
    result.append(arg)
    return result


print(works('a'))
print(works('b'))

# The ifx is to pass in something else to indicate the first call:


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy('a')
nonbuggy('b')

# @@ Explode/Gather Positional Arguments with *


def print_args(*args):
    print('Positional tuple:', args)


print_args()
print_args(3, 2, 1, 'wait!', 'uh...')


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the resut:', args)


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

print_args(2, 5, 7, 'x')

args = (2, 5, 7, 'x')
print_args(args)
print_args(*args)

# @@ Explode/Gather Keyword Arguments with **


def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# @@ Keyword-Only Arguments


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


print('#'*20)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print('#'*20)

print_data(data, start=4)
print('#'*20)

print_data(data, end=2)
print('#'*20)


# @@ Mutable and Immutable Arguments
outside = ['one', 'fine', 'day']


def mangle(arg):
    arg[1] = 'terrible!'


print(outside)
mangle(outside)
print(outside)
