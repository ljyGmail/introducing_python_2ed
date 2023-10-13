# @ Decorators

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

cooler_add_ints = document_it(add_ints)  # manual decorator assignment
print(cooler_add_ints(3, 5))

# An alternative to the manual decorator assignment


@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

# another decorator:


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

# The decorator that's used closest to the function runs first and then the one above it


@document_it
@square_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

# revere the decorator order


@square_it
@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
