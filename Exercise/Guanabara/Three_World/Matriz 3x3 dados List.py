matriz = [ [0,0,0], [0,0,0], [0,0,0] ]
par = cl3 = 0
for linha in range(0,3): #vai percorrer as linhas [[0,0,0]]
    for colunas in range(0,3): # vai percorrer as colunas ( 0,0,0 )
        matriz [linha] [colunas] = int(input(f'Digite um valor para esta [ {linha} e {colunas} ]: '))
print('===' * 30)
for linha in range(0,3):
    for colunas in range(0,3):
        if matriz [linha] [colunas] % 2 == 0:
            par += matriz [linha] [colunas]

        if linha == 2:
            cl3 += matriz [linha] [colunas]   
        print(f'[ {matriz [linha] [colunas] :^5} ]', end='')
    print()

print(par)
print(cl3)
print(max(matriz[1]))