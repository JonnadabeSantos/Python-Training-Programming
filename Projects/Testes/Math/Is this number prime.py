a = 85 # Is this number primer ?
prime = 0

for soma in range(1, a+1):
    rest = a % soma
    print(soma, rest)
    
    if rest == 0:
        prime += 1

if prime == 2:
    print(f'Numero {a} é primo')

else:
    print(f'Numero {a} não é primo')