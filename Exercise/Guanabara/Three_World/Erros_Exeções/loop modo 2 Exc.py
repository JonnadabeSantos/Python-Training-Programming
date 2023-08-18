def leiaInt(numb):
    while True:
        try:
            valor = int(input(numb))        
        except(ValueError, TypeError):
            print('\n\033[31mERROR ! Digite um numero Inteiro válido !\033[m')
            continue # << vai continuar o loop
        except(KeyboardInterrupt):
            print('\n\033[31mWEEEOE ! O usuário preferiu não digitar nenhum valor\033[m')
            return 0
        else:
            return valor
        


def leiaFloat(msg):
    while True:
        try:
            dec = float(input(msg))            
        except(ValueError, TypeError):
            print('\n\033[31mERROR ! Digite um numero Real válido !\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mWEEEOE ! O usuário preferiu não digitar nenhum valor\033[m')
            return 0
        else:
            return dec


n1 = leiaInt('Digite um Valor Inteiro: ')
n2 = leiaFloat('Digite um Valor Real: ')
print(f'O valor interiro foi {n1} e o real foi {n2}')
