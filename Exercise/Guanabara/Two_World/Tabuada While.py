while True:
    table = int(input('Number Tabuada ?: '))
    if table < 0:
        break
    
    print(f'='*50)
    for tb in range( 0 , 11 ):
        print(f'{tb} x {table} = { tb * table}')
    print(f'='*50)

print(f'Tabuada Encerrada ! Volte sempre.')