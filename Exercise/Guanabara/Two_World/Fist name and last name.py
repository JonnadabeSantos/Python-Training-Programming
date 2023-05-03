name = str( input('Type your name: ') ).lower() .strip() .split()

# Fist one condition
print('Your fist name is {} and last name is {}'.format(name[0], name[-1]))

# Second condition
print('Your fist name is {} and last name is {}'.format(name[0], name[len(name)-1]))

# In the second condition [ len()-1 ] will show the last list