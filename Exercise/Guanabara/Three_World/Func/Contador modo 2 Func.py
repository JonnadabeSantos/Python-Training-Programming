from time import sleep

def contador( i, f, p ):

    if p < 0:
        p *= -1
    
    if p == 0:
        p = 1
    
    print(f'Contagem de {i} até {f} de {p} em {p}: ')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep( 0.2 )
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep( 0.2 )
        print('FIM!')

print(f'\nDiga a Contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador( ini, fim, pas )