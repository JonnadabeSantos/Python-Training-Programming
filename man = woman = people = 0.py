man = woman = people = 0

cadastro = ' '
while not cadastro in 'Nn':
    print('='*60)
    print()

    menu = 'CADASTRO DE PESSOAS'
    print(menu.center(60, ' '))
    print() 

    idade = int(input('Type Years Old: '))
    sexo = input('Inform your gender [M/F]: ').strip() [0]

    if idade > 18:
        people += 1
    
    if sexo in 'Mm':
        man += 1

    if sexo in 'Ff' and idade < 20:
        woman += 1
    
    print()
    while True:
        cadastro = input('Do you wish to continue ? [S/N]: ').strip() [0]
        if cadastro in 'SsNn':
            break


print('='*60)
print()

menu = 'TOTAL DE PESSOAS CADASTRADAS'
print(menu.center(60, ' '))
print() 

print(f'''
Maiores de 18 Anos:             {people}
Homens:                         {man}
Mulheres menores de 20 Anos:    {woman}
''') 

  


