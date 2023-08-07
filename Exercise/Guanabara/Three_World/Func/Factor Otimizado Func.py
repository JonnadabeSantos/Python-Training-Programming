def fac(n,show=False):
    f = 1
    for c in range(n,0,-1):
        if show and c > 1:
            print(f'{c}', end=' x ')
        else:
            print(f'{c}', end=' = ')
        f *= c
    return print(f)

fac(7,True)    