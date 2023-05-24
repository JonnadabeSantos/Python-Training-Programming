soma = 0
media = 0
permission = ''

n1 = int(input('Type Number: '))
n2 = int(input('enter another number: '))
soma = (n1 + n2)
cont = 2

while not permission == 'N':
    if n1 > n2:
        maior = n1
      
    elif n1 < n2:
        maior = n2 

    permission = input('Do you wish to continue ? [S/N]: ').upper()
    if permission == 'S':
        n2 = int(input('enter another number: '))
        soma += n2
        cont += 1

print(f'\nThe average of all numbers is { soma / cont } and the largest number is {maior} !')
