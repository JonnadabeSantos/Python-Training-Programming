cont = soma = 0

while True:
    user = int(input('Type Number: '))

    if user == 999:
        break
    soma += user
    cont += 1

print(f'Were Typed {cont} Numbers and the sum between them is {soma}')