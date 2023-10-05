# @ Iterate with for and in
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

print('#' * 20)

for letter in word:
    print(letter)

print('#' * 20)

# @@ Cancel with break
word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)

print('#' * 20)

# @@ Skip with continue

# @@ Check break Use with else
word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")

print('#' * 20)

# @@ Generate Number Sequences with range()
for x in range(0, 3):
    print(x)

print(list(range(0, 3)))

for x in range(2, -1, -1):
    print(x)

print(list(range(2, -1, -1)))

print(list(range(0, 11, 2)))
