def fator(numero, show=False):
    cont = numero
    while cont > 1:
        if cont == numero:
            cont -= 1
            soma = cont *  numero
            if show:
                print(f'{numero} x {cont}', end=' x ')
        elif cont > 1:
            cont -= 1
            soma *= cont
            if show:
                if cont == 1:
                    print(f'{cont}', end=' = ')
                else:
                    print(f'{cont}', end=' x ')
    return print(soma)


print( '-' * 40)
x = int(input('Type Number: '))
w = input('Want to see calculation [Y/N] ?: ')
if w in 'Yy':
    w = True

fator( x, w)