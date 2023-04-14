while True:

    if not (nota := input(f'Nota entre "0" e "10": ')).isdigit() or (nota := int(nota)) < 1 or nota > 10:
        print('Valor INVÁLIDO!!')
    
    else:
        print('okk')