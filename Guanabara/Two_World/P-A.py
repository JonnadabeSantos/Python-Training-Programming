fist = int(input('Type fist: '))
razon = int(input('Type razon: '))
dec = fist + ( 10 - 1 ) * razon # ( 10 - 1 ) o '10' é o numero de termos 

for c in range ( fist, dec + razon, razon):
     print(f'{c}', end=' > ')