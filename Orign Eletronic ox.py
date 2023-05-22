while True:
    print('='*60)
    print()

    menu = 'JhonDabe Bank'
    print(menu.center(60, ' '))
    print() 
    print('='*60)
    print()

    ced = 50
    total_ced = 0 
    

    saque = input("What's value saq: ")
    while saque.isdigit():
        valor = int(saque)
        if valor >= ced:
            valor -= ced
            total_ced += 1
        
        else:
            if total_ced > 0:
                print(f'Total de {total_ced} cédulas de {ced}')
            
            if ced == 50:
                ced = 20
            
            elif ced == 20:
                ced = 10
            
            elif ced == 10:
                ced = 1

            if valor == 0:
                fim = 0
                break
    
    if fim == 0:
        break

print('The End')

