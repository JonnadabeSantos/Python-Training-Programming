soma = caro = barato = 0
lop = ' '

while not lop in 'Nn':
    print('='*60)
    print()

    menu = 'LOJA DE PRODUTOS'
    print(menu.center(60, ' '))
    print() 

    product = input('Inform Buy Product: ').strip()
    preco = float(input('Inform How Much: '))
    soma += preco

    if preco < barato or barato == 0:        
        barato = preco
        nome = product

    if preco > 1000:
        caro += 1

    print() 
    while True:
        lop = input('Do you wish to Continue? [Y/N]: ')
        if lop in 'YyNn':
            break   
   

print('='*60)
print()

menu = 'LOJA DE PRODUTOS'
print(menu.center(60, ' '))
print() 

print(f'''
Total de gasto na compra foi:   {soma}
Foram {caro} produtos maiores de 1000,00 R$ 
O produto mais barato é :       {nome} e custa R$ {barato}
''')


