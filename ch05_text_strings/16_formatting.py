# @ Formatting

# @@ Old style: %

# an integer
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

# a float
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

# an integer and a literal %
print('%d%%' % 100)

# interpolation
actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)
print('Our cat %s weighs %s punds' % (cat, weight))

thing = 'woodchuck'

print('%s' % thing)
print('%12s' % thing)
print('%+12s' % thing)
print('%-12s' % thing)
print('%.3s' % thing)
print('%12.3s' % thing)
print('%-12.3s' % thing)

# a float with %f variants:
thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%.3f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)

# an integer with %d:
thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)

# @@ New style: {} and format()
thing = 'woodchuck'
print('{}'.format(thing))

thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}'.format(thing, place))
# position
print('The {1} is in the {0}'.format(place, thing))
# named arguments
print('The {thing} is in the {place}'.format(thing='duck', place='bathtub'))

d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}'.format(d))

thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The {:10s} is at the {:10s}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing, place))
print('The {:^10s} is at the {:^10s}'.format(thing, place))
print('The {:>10s} is at the {:>10s}'.format(thing, place))
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))

# @@ Newest Style: f-strings
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')

print(f'The {thing:>20} is in the {place:.^20}')

print(f'{thing = }, {place = }')

print(f'{thing[4:] = }, {place.title() = }')

print(f'{thing = :>4.4}')
