numero = None
while not numero:
    entrada = input('Digite um número entre 1 e 10: ')
    if entrada.isdigit():
        numero = int(entrada)
        if numero < 1 or numero > 10:
            print('Você deve digitar um número que deve estar entre 1 e 10 !')
            numero = None
        else:
            print(f'Sua nota é {numero} !')

    else:
        print('Digite apenas números\n')

    