peso_1 = 0
peso_2 = 0
peso_3 = 0
peso_4 = 0
peso_5 = 0

for wheight in range(1, 6):
    w = float(input(f'Inform the wheight {wheight}º person: '))
    
    if wheight == 1:
        peso_1 += w


    elif wheight == 2:
        peso_2 += w
        if peso_2 > peso_1:
            maior = peso_2
            menor = peso_1
        else:
            maior = peso_1
            menor = peso_2
    

    elif wheight == 3:
        peso_3 += w
        if peso_2 < peso_3 > peso_1:
            maior = peso_3    
        
        elif peso_2 > peso_3 < peso_1:
            menor = peso_3



    elif wheight == 4:
        peso_4 += w
        if peso_3 < peso_4 > peso_2 and peso_4 > peso_1:
            maior = peso_4

        elif peso_3 > peso_4 < peso_2 and peso_4 < peso_1:
            menor = peso_4 

    else:
        peso_5 += w
        if peso_4 < peso_5 > peso_3 and peso_2 < peso_5 > peso_1:
            maior = peso_5
        
        elif peso_4 > peso_5 < peso_3 and peso_2 > peso_5 < peso_1:
            menor = peso_5

print(f'O maior peso é {maior}Kg e o menor peso é {menor}Kg')