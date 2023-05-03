menu ='''
[01] Somar
[02] Multiplicar
[03] Maior
[04] Novos Numeros
[05] Sair do Programa
'''

resut = None
while not resut:

    n1 = int(input('Type fist number: '))
    n2 = int(input('Type second number: '))

    select = int(input(f'{menu}Option Select: '))

    if select == 1:
        print(f'\nThe Sum {n1} + {n2} is {n1+n2}!\n')
        resut = 1  

    elif select == 2:
        print(f'\nThe Multiplication {n1} x {n2} is {n1*n2}!\n')
        resut = 1  

    elif select == 3:
        if n1 > n2:
            print(f'\n{n1} is bigger than {n2}\n')         
            resut = 1  

        elif n2 > n1:
            print(f'\n{n2} is bigger than {n1}\n')
            resut = 1  

        else:
            print(f'\n{n1} is equal {n2}\n')
            resut = 1  
            
    elif select == 4:
        print('\n')
        resut = None

    elif select == 5:
        print('\n')
        resut = 1            
