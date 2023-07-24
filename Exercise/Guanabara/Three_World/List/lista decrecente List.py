decre = []

while True:   
    decre.append(int(input('Type Number: ')))
    perg = input('Do was the continue [Y/N] ? ')    
    if perg in 'Nn':
        break

decre.sort( reverse=True )

print(f'''
O total de numeros digitados foram {len(decre)}
A lista decrescente é {decre}
O numero 5 {'Está' if 5 in decre else 'Não está'} na lista !
      ''')

