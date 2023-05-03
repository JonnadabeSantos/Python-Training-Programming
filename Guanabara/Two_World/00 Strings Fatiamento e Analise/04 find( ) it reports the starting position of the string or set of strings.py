n1 = 'valdomiro silva cacete'
n2 = 'metimozerque napomuceno cardoso cavalcante'
n3 = 'josadarque pereira de pinto sega'

print(n1.find('silva'))
print(n1[9:11])

print(n3.find('c')) # not exist !

#o primeiro 'a' é encontrado na posição[3] e ele aparece 3 vezes na .count('a')
# the first 'a' is found at position[3] and it appears 3 times in .count('a')

print(n3.find('a'), n3[3], n3.count('a'))

print(n2.find('car'), n2[24:]) # start
print(n2.find('cav'), n2[24:31] ,'\n') # end

