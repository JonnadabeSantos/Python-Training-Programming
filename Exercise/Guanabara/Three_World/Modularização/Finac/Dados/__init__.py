from Finac.Dinheiro import moeda

def validação( va, li, dar ):
    if va.isdigit():
        print('x')
        va = va.replace( ',', '.' )
        float(va)
    
    if li.isdigit():
        print('z')
        li = li.replace( ',', '.' )
        li = li.replace( ',', '.' )

    if dar.isdigit():
        print('y')
        dar = dar.replace( ',', '.' )
        dar = dar.replace( ',', '.' )
    
    else:
        print('Error')
