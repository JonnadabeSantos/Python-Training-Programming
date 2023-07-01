glob = []
people = []
leve = []
pesado = []

while True:
    people.append(input('Type Name: '))
    people.append(int(input('Type Yeers Old: ')))
    glob.append(people[:])
    people.clear()

    resp = input('\nDeseja continuar [Y/N] ?')
    if resp in 'Nn':
        break

for lista in glob:
    for peso in lista:
                
        if peso.isdigit():
            if peso >= 100:
                pesado.append(peso)
            
            elif peso <= 70:
                leve.append(peso)

print(f'o maior peso foi {max(pesado)} e as pessoas mais pesadas foram {pesado}')
print(f'O menor peso foi {min(leve)} e as pessoas mais leves são {leve}')
print(f'O total de pessoas cadastradas foram {len(glob)}')