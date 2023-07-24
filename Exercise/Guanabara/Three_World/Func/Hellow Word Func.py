def helow(mundo):
    
    if len(mundo) < 4:
        print(f'~' * len(mundo) )
        print(str(mundo).center(len(mundo) ) )
        print(f'~' * len(mundo) )
    else:
        print(f'~' * ( 5 + len(mundo) ) )
        print(str(mundo).center( 5 + len(mundo) ) )
        print(f'~' * ( 5 + len(mundo) ) )


txt = input('Degite algo: ')
helow(txt)