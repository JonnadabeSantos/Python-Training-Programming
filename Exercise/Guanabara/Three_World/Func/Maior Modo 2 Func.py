from time import sleep

def maior( * numb ):
    cont = max = 0
    sleep( 1 )
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in numb:
        print(f'{valor} ', end='')
        sleep( 1 )

        if cont == 0:
            max = valor
        else:
            if valor > max:
                max = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {max}.')


maior(0)
maior(5)
maior(1,5,9)
maior(0,1,4,5,9,2)
maior(9,2)