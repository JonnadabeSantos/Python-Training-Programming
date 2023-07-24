lista = ( 'caneta', 1.50, 'biscoito', 3, 'sapato', 150, 'livro', 35.54, 'aroz', 6, 'caderno', 12 )

print('><><><'*10)
print(f'{"LISTA DE PREÇOS":^60}')
print('><><><'*10)

for preço in range(0, len(lista)):
    if preço % 2 == 0:
        print(f'{lista[preço]:.<30}R$', end='')

    else:
        print(f'{lista[preço]:>7.2f}')



print(f'')