matriz = [ [0,0,0], [0,0,0], [0,0,0] ]

for linha in range(0,3): #vai percorrer as linhas [[0,0,0]]
    for colunas in range(0,3): # vai percorrer as colunas ( 0,0,0 )
        matriz [linha] [colunas] = int(input(f'Digite um valor para esta [ {linha} e {colunas} ]: '))
print('===' * 30)
for linha in range(0,3):
    for colunas in range(0,3):
        print(f'[ {matriz [linha] [colunas] :^5} ]', end='')
    print()