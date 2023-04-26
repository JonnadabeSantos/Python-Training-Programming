soma = 0

for n in range ( 1, 7):
    number = int(input('Type Number: '))

    if number % 2 == 0:
        soma += number
        
print(f'\nsum of even numbers are {soma}')
