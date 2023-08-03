def voto(old):
    from datetime import date
    idade = ( date.today().year ) - old    

    if 18 > idade >= 16 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'        
    
    else:
        return f'Com {idade} anos: NÃO VOTA'
        

    
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))