fibouser = int(input('Type Term: '))

fibostart = 1
fibomed = 0

print(f'{fibomed} → {fibostart}', end='')

cont = 3

while cont <= fibouser:
    fibonacci = fibostart + fibomed
    print(f' → {fibonacci}', end='')
    
    fibomed = fibostart
    fibostart = fibonacci

    cont += 1