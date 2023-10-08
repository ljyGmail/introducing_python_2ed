# @ Inner Functions
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print(outer(4, 7))


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)


print(knights('Ni!'))

# @@ Closures


def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2


a = knights2('Dock')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a)
print(b)

print(a())
print(b())
