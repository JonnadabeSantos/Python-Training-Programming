from Finac import moeda

p = float(input('Digite o Preço: R$ '))
print(f'O dobro de {moeda.mod((p))} é {moeda.mod(moeda.dobro(p))}')
print(f'A metade de {moeda.mod((p))} é {moeda.mod(moeda.metade(p))}')
au = int(input('Deseja aumantar quantos %?: '))
print(f'A metade de {moeda.mod((p))} em {au}% é {moeda.mod(moeda.aumentar(p,au))}')
red = int(input('Deseja reduzir quantos %?: '))
print(f'A metade de {moeda.mod((p))} em {red}% é {moeda.mod(moeda.reduzir(p,red))}')



