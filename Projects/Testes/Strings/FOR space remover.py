diga = input('diga um texto: ')

# este mecanismo é usado para retirar espaços ou pa adicionar elementos entre em vez dos espaços ===========
fracao = diga.split()
colar = ''.join(fracao)
# ==========================================================================================================


inverso = ''

for elemento in range(len(colar) - 1, -1, -1):
    inverso += colar[elemento]

if inverso == colar:
    print(f'Temos um políndromo pois {colar} é igual a {inverso}')

else:
    print(f'Não temos um políndromo pois {colar} não é igual a {inverso}')