fist = int(input('Type fist: '))
razon = int(input('Type razon: '))
term = int(input('Type Term: '))
count = 0
soma = 0

while count < term:
    print(f'{fist}', end=' → ')
    soma += fist
    fist += razon
    count += 1

print(f'The Sum all term is {soma}')