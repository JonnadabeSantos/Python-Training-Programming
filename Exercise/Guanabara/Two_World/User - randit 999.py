soma = 0
cont = 0
user = int(input('Type Number: '))

while not user == 999:
    print(f'\n{user}')
    soma += user
    cont += 1
    user = int(input('Type Number: '))
    
print(f'foram digitados {cont} vezes e a soma dos numeros gerados são {soma}')


