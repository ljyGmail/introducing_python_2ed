# @ Strip with strip()

import string
world = '     earth     '
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())
print(world.strip('!'))

# strip multi-characters
blurt = "What the ...!!?"
print(blurt.strip('.?!'))
print('#' * 20)

# some definitions of character groups
print(string.whitespace)
print('#' * 20)
print(string.punctuation)

blurt = 'What the...!!?'
print(blurt.strip(string.punctuation))

prospector = 'What in tarnation ...??!!'
print(prospector.strip(string.whitespace+string.punctuation))
