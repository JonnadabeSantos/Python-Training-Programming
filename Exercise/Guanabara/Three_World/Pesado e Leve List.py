glob = []
people = []
leve = []
pesado = []
maior = menor = 0

while True:
    people.append(input('Type Name: '))
    people.append(int(input('Your Weight : ')))
    if len(glob) == 0:
        maior = menor = people[1]
    else:
        if people[1] > maior:
            maior = people[1]
        if people[1] < menor:
            menor = people[1]

    glob.append(people[:])
    people.clear()

    resp = input('\nDeseja continuar [Y/N] ?')
    if resp in 'Nn':
        break

for lista in glob:
    if lista[1] >= 100:
        pesado.append(lista[0])
    
    elif lista[1] <= 70:
        leve.append(lista[0])


print(f'o maior peso foi {maior} e as pessoas mais pesadas foram {pesado}')
print(f'O menor peso foi {menor} e as pessoas mais leves são {leve}')
print(f'\nO total de pessoas cadastradas foram {len(glob)}')