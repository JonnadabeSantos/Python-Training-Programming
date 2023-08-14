from Finac import moeda

p = float(input('Digite o Preço: R$ '))
print(f'O dobro de {moeda.mod((p))} é {moeda.dobro( p, True )}')
print(f'A metade de {moeda.mod((p))} é {moeda.metade( p )}')
au = int(input('Deseja aumantar quantos %?: '))
print(f'O aumento de {moeda.mod((p))} em {au} % é { moeda.aumentar( p, au, True )}')
red = int(input('Deseja reduzir quantos % ?: '))
print(f'A Redução de {moeda.mod((p))} em {red} % é {moeda.reduzir( p, red)}')



