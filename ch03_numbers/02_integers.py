# @ Integers

# @@ Literal Integers
print(5)
print(0)

# invalid token
# print(05)

print(123)
print(+123)
print(-123)

# can't have commas in the integer: (you'll get a tuple)
print(1, 000, 000)

# but you can use underscore as a digit separator:
print(1_000_000)
print(1_2_3)
print('#' * 20)

# @@ Integer Operations
print(5 + 9)
print(100 - 7)
print(4 - 10)

print(5 + 9 + 3)
print(4 + 3 - 2 - 1 + 6)

# not required to have a space between each number and operator:
print(5+9 + 2)

print(6 * 7)
print(7 * 6)
print(6 * 7 * 2 * 3)

# floating-point (decimal) division
print(9 / 5)
# integer (truncating) division
print(9 // 5)

# ZeroDivisionError:
# print(5 / 0)
# print(7 // 0)
print('#' * 20)

# @@ Integers and Variables
a = 95
print(a)
print(a - 3)

# the value of a did not change
print(a)

# change the value of a
a = a - 3
print(a)

a = 95
temp = a - 3
a = temp
print(a)

# combine the arithmetic operators with assignment:
a = 95
a -= 3
print(a)

a = 92
a += 8
print(a)

a = 100
a *= 2
print(a)

a = 200
a /= 3
print(a)

a = 13
a //= 4
print(a)

print(9 % 5)
# get both the (truncated) quotient and remainder at once:
print(divmod(9, 5))

print(9 // 5)
print(9 % 5)

print(2 ** 3)
print(2.0 ** 3)
print(2 ** 3.0)
print(0 ** 3)
print('#' * 20)

# @@ Precedence
print(2 + 3 * 4)
print(2 + (3 * 4))

print(-5 ** 2)
print(-(5 ** 2))
print((-5) ** 2)
print('#' * 20)

# @@ Bases
print(10)
print(0b10)
print(0o10)
print(0x10)

# convert an integer to a string with any of these bases:
value = 65
print(bin(value))
print(oct(value))
print(hex(value))

# chr() function converts an integer to its single-character string equivalent:
print(chr(65))

# ord() goes the other way:
print(ord('A'))
print('#' * 20)

# @@ Type Conversions
print(int(True))
print(int(False))

print(bool(1))
print(bool(0))

print(int(98.6))
print(int(1.0e4))

print(bool(1.0))
print(bool(0.0))

print(int('99'))
print(int('-23'))
print(int('+12'))
print(int('1_000_000'))

# If the string represents a nondecimal integer, include the base:
print(int('10', 2))  # binary
print(int('10', 8))  # octal
print(int('10', 16))  # hexadecimal
print(int('10', 22))  # chesterdigital

print(int(12345))

# ValueError
# int('99 bottles of beer on the wall')
# int('98.6')

print(4 + 7.0)
print(True + 2)
print(False + 5.0)
print('#' * 20)

# @@ How Big Is an int?
google = 10 ** 100
print(google)
print(google * google)
