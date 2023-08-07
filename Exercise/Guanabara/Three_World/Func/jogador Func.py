def player(nome, gol):
    if not nome:
        nome = '< desconhecido >'

    if not gol:        
        gol = '0'

    elif gol.isdigit():
        int(gol)
       
    else:
        gol = '??'

    return print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

print( '-' * 40 )
jogador = input('Nome do jogador: ')
gool = input('Número de Golds: ')
player( jogador, gool )
