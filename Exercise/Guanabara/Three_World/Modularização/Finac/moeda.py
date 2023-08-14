def metade( met=0, show=False ):
    if show:
        rest = f'R$ { ( met / 2 ):>.2f}'.replace('.',',')
        return rest
    else:
        return met / 2

def dobro( dob=0, show=False ):   
    rest = dob * 2
    return rest if show is False else mod( rest )
          

def reduzir( val=0, porc=0, show=False ):
    
    rest = val * ( 1 - ( porc / 100 ) )
    return rest if not show else mod ( rest )
   

def aumentar( aum=0, poc=0, show=False ):
    
    rest = aum * ( 1 + ( poc / 100 ) )
    return mod( rest ) if show else rest
   

def mod(preco=0, und='R$ '):
    return f'{und}{preco:>.2f}'.replace('.',',')


def resumo( dinheiro=0, aumento=0, redução=0 ):
    print( '-' * 40 )
    print( 'RESUMO DO VALOR'.center( 40 ) )
    print( '-' * 40 )

    extrato = f'''
preço analisado:\t{mod( dinheiro )}
Dobro do preço:\t\t{dobro( dinheiro, True )}
Metade do preço:\t{metade( dinheiro, True )}
{aumento} % de aumento:\t{aumentar( dinheiro, aumento, True )}
{redução} % de redução:\t{reduzir( dinheiro, redução, True )}
'''
    return print( extrato ) , print( '-' * 40 )