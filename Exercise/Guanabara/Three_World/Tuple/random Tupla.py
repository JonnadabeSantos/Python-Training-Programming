from random import randint
Ai = ( randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10) )


print(f'Os numeros sorteados foram:', end=' ')


for tuple in Ai:    
    print(tuple, end=' ')

print(f'\nO maior numero foi {max(Ai)} e o menor foi {min(Ai)}')