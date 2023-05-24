v1 = ( int(input('Type Value 1: ')), 
      int(input('Type Value 2: ')), 
      int(input('Type Value 3: ')), 
      int(input('Type Value 4: ')))

print(f'Voce digitou o numero 9 {v1.count(9)}x vezes')

if 3 in v1:
    print(f'O valor 3 esta na {v1.index(3)+1}ª posição ')

else:
    print('O Valor 3 não foi digitado !')

print('Os numeros pares são: ', end='')

for par in v1:
    if par % 2 == 0:
        print(f'{par}', end=' ')
