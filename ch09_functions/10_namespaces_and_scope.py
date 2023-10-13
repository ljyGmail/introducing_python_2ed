# @ Namespaces and Scope

animal = 'fruitbat'


def print_global():
    print('inside print_global:', animal)


print('at the top level:', animal)
print_global()


def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)


# UnboundLocalError
# change_and_print_global()


def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))


change_local()
print(animal)
print(id(animal))

animal = 'fruitbat'


def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)


print(animal)
change_and_print_global()
print(animal)
print('#' * 20)

animal = 'fruitbat'


def change_local():
    animal = 'wombat'  # local variable
    print('locals:', locals())


print(animal)
change_local()
print('globals:', globals())
print(animal)
