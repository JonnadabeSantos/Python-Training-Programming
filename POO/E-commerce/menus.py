def linha( aling = 45 ):
    return ('-' * aling )

def cabeçalho( txt, linhaCab = 45 , line = 'both' ):
    cab = f'{ txt.center(linhaCab) }'
    
    if line == 'top':
        return f'{linha(linhaCab)}\n{cab}'
    
    elif line == 'bottom':
        return f'{cab}\n{linha(linhaCab)}'

    elif line == 'both':
        return f'{linha(linhaCab)}\n{cab}\n{linha(linhaCab)}\n'
    
    elif line == None:
        return cab


def COMAdecimal( valor ):
    txt = str( valor )
    txt = txt.replace( '.0', ',00' )
    txt = txt.replace( '.', ',' )
    return txt