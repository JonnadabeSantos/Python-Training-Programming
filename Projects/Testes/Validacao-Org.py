while not (nota := input(f'Nota entre "0" e "10": ')).isdigit() or (nota := int(nota)) < 0 or nota > 10:
    print('Valor INVÁLIDO!')

print(nota)