

s = 0
c = 0
for x in range(1, 501, 2):
    
    if x % 3 == 0:
        
        s += x 
        c += 1
        
print(f'\nSoma dos {c} numeros primos é {s}')

print(f'\neles são:\n')

for x in range(1, 501, 2):
    
    if x % 3 == 0:
        
        s += x 
        print(x, end = ' ')

print('\n')