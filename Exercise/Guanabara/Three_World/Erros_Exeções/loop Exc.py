def leiaInt():
    while True:
        try:
            numb = int(input('Digite um Numero inteiro: '))
            break
        except:
            print('\nERROR ! Digite um numero Inteiro válido !')


def leiaFloat():
    while True:
        try:
            dec = float(input('Digite um numero decimal: '))
            break
        except:
            print('\nERROR ! Digite um numero Real válido !')
            


leiaInt()
leiaFloat()
