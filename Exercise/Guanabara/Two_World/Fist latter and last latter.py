name = str(input('Type your name: ')).lower() .strip()

print('\nYour name has {} letters "a"'.format(name.count('a')))
print('the first one starts at position {}'.format(name.find('a')+1) )
print('and the last one is at position {}\n' .format(name.rfind('a')+1) )

print(name[3:6])
