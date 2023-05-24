from datetime import date
data = date.today().year

adult = 0
menor = 0

for ano in range(1, 8):
    idade = int(input(f'inform the year of birth of the {ano}ª person: '))
    maior = data - idade

    if maior < 21:
        adult += 1

    else:
        menor += 1

print(f'\nin total {adult} people are adult and {menor} people are not adult \n')