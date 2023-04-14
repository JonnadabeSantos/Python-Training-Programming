import random

n1 = input('primeiro nome: ')
n2 = input('segundo nome: ')
n3 = input('terceiro nome: ')
n4 = input('quarto nome: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

#Shuffle >> vai embaralhar a lista e vai sortear cada item da lista um por um

print(f'A ordem do Sorteio é {lista}')

#Forma Simplificada

from random import shuffle

n1 = input('primeiro nome: ')
n2 = input('segundo nome: ')
n3 = input('terceiro nome: ')
n4 = input('quarto nome: ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print(f'A ordem do Sorteio é {lista}')