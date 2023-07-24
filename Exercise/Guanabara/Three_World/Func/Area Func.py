def linha(msg):
    print( '-' * 30 )
    print(msg)
    print( '-' * 30 )

def area(l,c):
    m = l * c
    print(f'A área de {l} x {c} é {m}m²')

linha('Cáculo de Area'.center(30))
area(float(input('Informe a largura: ')), float(input('Informe o comprimento: ')))