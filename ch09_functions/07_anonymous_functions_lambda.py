# @ Anonymous Functions: lambda

def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):  # give that prose more punch
    return word.capitalize() + '!'


edit_story(stairs, enliven)

# lambda
edit_story(stairs, lambda word: word.capitalize() + '!')
