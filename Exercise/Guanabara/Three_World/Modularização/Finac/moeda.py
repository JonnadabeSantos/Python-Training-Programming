def metade(met):
    return met / 2

def dobro(dob):
    return dob * 2

def reduzir(val, porc):
    return val * ( 1 - ( porc / 100 ) )

def aumentar(aum, poc):
    return aum * ( 1 + ( poc / 100 ) )

def mod(preco=0, und='R$ '):
    return f'{und}{preco:>.2f}'.replace('.',',')