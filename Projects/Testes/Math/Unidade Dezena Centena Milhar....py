# result at the math

numero = int(input('Digite um numero entre 0 a 9999: '))
unidade = numero % 10

numero = ( numero - unidade ) / 10
dezena = int(numero % 10)

numero = ( numero - dezena ) / 10
centena = int( numero % 10 )

numero = ( numero - centena ) / 10
milhar = int( numero % 10 )


print(f'\nEste número matematicamente tem {milhar} milhar, {centena} centena, {dezena} dezena, {unidade} unidade.')



# result at the Strings

numero_string = str( milhar*1000 + centena*100 + dezena*10 + unidade)

print(f'Este Número em string tem {numero_string[0]} milhar, {numero_string[1]} centena', end = ' ')
print(f'{numero_string[2]} dezena, {numero_string[3]} unidade\n')