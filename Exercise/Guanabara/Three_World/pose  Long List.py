lista = []
maior = 0
menor = 0

for number in range(0, 5):
    lista.append(int(input(f'Type {number+1}º Number: ')))
    
    if number == 0:
        maior = menor = lista[number]

    else:
        if lista[number] > maior:
            maior = lista[number]

        elif lista[number] < menor: 
            menor = lista[number]

print(f'Sua lista é {lista}')
print(f'\nO maior valor é {maior} e esta na posição ', end='')

for pos, value in enumerate(lista):
    if value == maior:
        print(f'{pos+1}', end='...')

print(f'\nO menor valor é {menor} e esta na posição ', end='')

for pos, value in enumerate(lista):
    if value == menor:
        print(f'{pos+1}', end='...')

