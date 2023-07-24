alunos = []
nome = [0,[0,0]]

while True:
    for linha in range(0,2):
        if linha == 0:
            nome[0] = input('Type Name: ')
        else:        
            for coluna in range(0,2):
                nome[linha][coluna] = float(input(f'Type Note 0{coluna + 1}: '))
    
    alunos.append(nome[:])
    nome.clear()
    nome = [0,[0,0]]


    while True:
        perg = input('\nDo you was to continue ?[Y/N]: ')
        if perg in 'YyNn':
            break
    
    if perg in 'Nn':
        break



print('--' *30)
print('Nº\tName\t\t\tMedia')
print('--' *30)

for n, name in enumerate(alunos):
    print(f'{n+1}\t{name[0]}\t\t\t{ ( name[1][0] + name[1][1] ) / len(name[1]):.2f}')

while True:
    perg = input('\nDo you want to make a new search [Y/N]?')
    if perg in 'Yy':
        while True:
            search = int(input('search grades by students: '))
            print(f'{alunos[search-1][0]} note is {alunos[search-1][1]}')
            while True:
                perg = input('\nDo you want to make a new search [Y/N]?')
                if perg in 'YyNn':
                    break
            if perg in 'Nn':
                break

    if perg in 'Nn':
        break

print('Thank You See You Later'.center(50,'-'))