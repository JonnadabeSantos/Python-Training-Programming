number = []

while True:
    value = int(input('Type Number: '))
    if value not in number:
        number.append(value)
        print('successfully added value !')    
    else:
        print('value not added successfully !')
    
    cont = input('\nDo you wish to continue [Y/N]?: ')
    if cont in 'Nn':
        break

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==')
print(f'you entered the values: {sorted(number)}')