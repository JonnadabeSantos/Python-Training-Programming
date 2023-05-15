from random import randint
soma = cont = 0

while True:
    user = input('Ímpar ou Par ? [I/P]: ').strip() [0]
    

    while user in 'PpIi' and soma == 0:
        number = int(input('Type Number: '))
        Ai = randint(0,10)
        soma = Ai + number      
    
    if user in'Pp':
        if soma % 2 == 0:
            print(f'Você é par escolheu o Numero {number} e seu oponente {Ai} logo {soma} é Par Voce Ganhou !\n')
            cont += 1
            # soma = 0
        else:
            print(f'Você é par escolheu o Numero {number} e seu oponente {Ai} logo {soma} é Impar Voce perdeu !\n')
            break

    if user in 'Ii':
        if soma % 2 == 1:
            print(f'Você é impar escolheu o Numero {number} e seu oponente {Ai} logo {soma} é Impar Voce Ganhou !\n')
            cont += 1
            # soma = 0
    
        else:
            print(f'Você é impar escolheu o Numero {number} e seu oponente {Ai} logo {soma} é Par Voce perdeu !\n')
            break


if cont > 0:
    print(f'Parabéns você Ganhou {cont} x consecutivas !\n')
    
else:
    print(f'Desculpe você não ganhou nenhuma vez tente novamente !\n')