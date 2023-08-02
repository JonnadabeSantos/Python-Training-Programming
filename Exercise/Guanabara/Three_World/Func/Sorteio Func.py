from random import randint
sort = []

def sorteio():
    print('\nSorteando 5 valores da Lista: ', end='')
    for x in range( 0,5 ):
        sort.append(randint(1,30))
    for valores in sort:
        print(f'{valores} ', end='')
    print('PRONTO!')

def somatorio(soma):
    adição = 0
    for ad in soma:
        if ad % 2 == 0:
            adição += ad
    print(f'Somando os valores pares de {soma}, temos {adição}',)



sorteio()
somatorio(sort)