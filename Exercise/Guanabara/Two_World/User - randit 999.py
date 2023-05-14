from random import randint

soma = 0
cont = 0
user = int(input('Type Number: '))

while not user == 999:
    Ai = randint(0,999)
    print(f'\n{Ai}')
    soma += Ai
    cont += 1
    user = int(input('Type Number: '))
    
print(f'foram digitados {cont} vezes e a soma dos numeros gerados são {soma}')


