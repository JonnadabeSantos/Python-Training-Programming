from random import randint

ai = randint(0,10)
chut = int(input('Type number: ').strip())
count = 0


while not chut == ai:    
    ai = randint(0,10)
    chut = int(input(f'errou o numeor foi {ai} ! Type number: ').strip())
    count += 1

print(f'Parabéns voce acertou o numero foi {chut} você precisou de {count}x para conseguir')