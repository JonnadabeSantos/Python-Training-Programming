maior = 0
menor = 0

for wheight in range(1,6):
    peso = float(input(f'Peso da {wheight}ª pessoa: '))

    if wheight == 1:
        maior = peso
        menor = peso
    
    else: 
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso é {maior}Kg e o menor é {menor}Kg')
