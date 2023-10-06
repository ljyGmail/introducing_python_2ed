# @ Get a Substring with a Slice

letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[:])
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])

print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:5])

# step backward
print(letters[-1::-1])
print(letters[::-1])

# Slices are more forgiving of bad offsets than are single-index lookups with [].
print(letters[-50:])
print(letters[-51:-50])
print(letters[:70])
print(letters[70:71])
