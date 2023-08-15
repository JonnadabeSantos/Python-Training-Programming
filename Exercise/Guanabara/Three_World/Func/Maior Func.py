from time import sleep
def maior( * numb ):
    sleep( 1 )
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep( 0.5 )

    print(f'Foram informados', end=' ')
    
    for ind in numb:
        print(f'{ind}', end=' ')
        sleep( 0.8 )
    
    if max(numb) == 0:
        print(f'ao todo foram 0 valores')
    else:
        print(f'ao todo foram {len(numb)} valores')
    print(f'O Maior valor informado foi {max(numb)}')
    

valor = int(input('Type value: '))
raize = int(input('Enter the raise: '))
reduce = int(input('Enter the reduce: '))    
maior(4)
maior(2,3,4)
maior(9,3,4,6)
maior( valor, raize, reduce )