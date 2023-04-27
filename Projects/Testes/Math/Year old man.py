soma = 0
man = 0
woman = 0

for static in range( 1, 5 ):
    name = input(f'\nInform {static}º name: ')
    idade = int(input(f'Inform {static}º years old: ' ))
    sexy = input(f'You is "M" or "F" : ')

    soma += idade

    if sexy in 'Mm': # valida o "M" Maiúsculo ou menúsculo "m"
        if idade > man:
            man = idade
            nome = name
    else:
        if idade < 20:
            woman += 1

print(f'\nA média da idade do grupo é { soma / 4 }')
print(f'O nome do homem mais velho é {nome}')
print(f'{woman} mulheres são menores que 20 anos\n')