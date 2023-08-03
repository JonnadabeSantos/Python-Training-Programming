def idade(old):
    from datetime import date
    idade = ( date.today().year ) - old
    return idade


def voto(idade):

    if 18 > idade >= 16 or idade >= 65:
        opção = 'VOTO OPCIONAL'
        return opção
    
    elif idade >= 18:
        opção = 'VOTO OBRIGATÓRIO'
        return opção
    
    else:
        opção = 'NÃO VOTA'
        return opção

    
nasc = int(input('Em que ano você nasceu? '))
print(f'\nCom { idade(nasc) } anos: {voto(idade(nasc))}')