soma = 0
cont = 0

for n in range ( 1, 7):
    number = int(input(f'Type the {n}º Number: '))

    if number % 2 == 0:
        soma += number
        cont += 1
        
print(f'\nsum of even {cont} numbers are {soma}')
