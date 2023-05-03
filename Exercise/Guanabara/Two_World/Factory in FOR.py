factor = int(input('Type Number: '))
print(f'Factory {factor}! = ', end='')

for f in range(factor, 1, -1):
    if f == factor:
        print(f'{f} x {f-1} ', end='' )
    
    elif f > 1:
        print(f'x {f-1} ', end='')
        
    rt = factor * (f -1)    
    factor = rt
   
print(f'=',factor,'\n')

# Option 2

numero = int(input('Digite um valor para ver seu fatorial: '))
fatorial = 1

for c in range(numero, 0, -1):
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    fatorial *= c
print(fatorial)