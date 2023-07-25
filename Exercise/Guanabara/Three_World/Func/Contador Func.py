from time import sleep

def linha():
    print('=-=' * 20)
def contagem( inicio, fim, passo):
    for c in range( inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(0.3)
    print('Fim!\n')


linha()
print(f'Contagem de 1 até 10 de 1 em 1')
for inicio in range(1,11):
    print(f'{inicio}', end=' ')
    sleep(0.1)
print('FIM!\n')

linha()
print('Contagem de 10 até 0 de 2 em 2')
for regresso in range( 10, -1, -2 ):
    print(f'{regresso}', end=' ')
    sleep(0.1)
print('FIM\n')

linha()
print(f'Qual é a sua contagem ?: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

linha()
print(f'Contagem de {i} até {f} de {p} em {p}:')

if p == 0:
    p += 1
    print('x')
if i > f and p > 0:
    p *= -1
    print('z')

if i > f:
    print('y')
    contagem( i, f - 1, p)
else:
    print('w')
    contagem( i, f + 1, p)