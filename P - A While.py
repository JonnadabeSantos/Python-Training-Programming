fist = int(input('Type fist: '))
razon = int(input('Type razon: '))
term = int(input('Type Term: '))

one = fist
count = 0
loop = 0
soma = 0
add = 0

while loop == 0:

    while count < term: 

        if count > (term - 2):
            print(f'{fist}', end=' ')
            soma += fist
            fist += razon
            count += 1
        
        if count == term:
            print('\n')    
            add = int(input('want to add more terms?: '))

            if add != 0:
                term += add
                count = 0
                fist = one
            else:
                loop = 1
                print(f'The count terms is {count} and sum all terms is {soma}\n')
        
        else:
            print(f'{fist}', end=' → ')        
            soma += fist
            fist += razon
            count += 1
