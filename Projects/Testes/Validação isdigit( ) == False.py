numero = None
while not numero:
    entrada = input('Digite uma letra: ')
    if entrada.isdigit() == False:   
        numero = (entrada).lower()     
        if numero == 'a' or numero == 'b':
            print('Você deve digitar letras em minúsculas !')
            numero = None
        else:
            print(f'Sua letra é {numero} !')

    else:
        print('Digite apenas Letras\n')

# nesta situação tudo que não for número será aceito !
# inclusivo caracteres especiais e espaços    