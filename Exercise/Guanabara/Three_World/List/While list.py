number = []
lop = 's'
while True:
    
    if lop in 'Ss':    
        user = int(input('Type Number list: '))

        if user in number:
            print('Duplicate number! enter another number...\n')                    
        else:
            print('Number successfully added...\n')
            number.append(user)
        
        while True:
            lop = input('Do you wish to continue? [S/N]: ').strip() [0]
            if lop in 'SsNn':
                break
    
    elif lop in 'Nn':
        break            

number.sort()              
print(f'Your list is {number}')