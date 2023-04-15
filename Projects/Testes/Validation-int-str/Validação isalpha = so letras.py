numero = None
while not numero:
    entrada = input('Digite uma letra: ')
    if entrada.isalpha():   
        numero = entrada.lower()     
        if numero == 'a' or numero == 'b':
            print('Você deve digitar letras em minúsculas !')
            numero = None
        else:
            print(f'Sua letra é {numero} !')

    else:
        print('Digite apenas Letras\n')

# nesta situação so é possível digitar letras
# qualquer coisa != de letras serão recusado inclusive espaços e caracteres especiais