# @ Escape with \

palindrome = 'A man,\nA plan,\nA canal:\nPanama'
print(palindrome)

print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')

testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
print(testimony)

fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105"
print(fact)

speech = 'The backslash (\\) bends over backwards to please you.'
print(speech)

# raw string
info = r'Type a \n to get a new line in a normal string'
print(info)

# A raw string does not undo (not '\n') any real newlines:
poem = r'''Boys and girls, come out to play.
The moon doth shine as bright as day.'''
print(poem)
