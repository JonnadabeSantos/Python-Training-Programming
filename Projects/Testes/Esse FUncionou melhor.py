while True:

    if not (nota := input(f'Digite uma nota entre "0" e "10": ')).isdigit() or (nota := int(nota)) < 1 or nota > 10:
        print('Valor Inválido !!\n')
    
    else:
        print('\nSua nota é:',nota)
        break