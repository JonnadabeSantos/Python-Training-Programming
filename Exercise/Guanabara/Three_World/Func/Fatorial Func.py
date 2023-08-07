def factor(number, show=False):
    for n in range ( number, 1 , -1 ):
        if n == number:      
            s = number * ( n - 1 )
            if show == True:
                print(f'{n}', end=' x ')

        else:
            s = s * ( n -1 )
            if show == True:
                print(f'{n}', end=' x ')
                if n == 2:
                    print( '1', end=' = ' )
    return s


print( '-' * 40 )
x = int(input('number: '))
w = input('want to see the calculation [Y/N}?: ')
if w in 'Yy':
    w = True

print(factor( x,w ))