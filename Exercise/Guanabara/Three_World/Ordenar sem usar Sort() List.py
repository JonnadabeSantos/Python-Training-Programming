lista = []

for valor in range(0,5):
    user = int(input('Tuper Number: '))

    if valor == 0 or user > lista[-1]:
        lista.append(user)
        print('Valor adicionado na ultima posição!\n')
    
    else:
        pos = 0
        while pos < len(lista):
            if user <= lista[pos]:
                lista.insert(pos , user)
                print(f'Valor adicionado na posição {pos} !\n')
                break      
            pos += 1

print('-='*30)
print(f'os valores digitados foram {lista}')