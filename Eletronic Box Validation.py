inicio = 'start'
ced = 50
total_ced = 0 
fim = 1
opercao = 0

while inicio == 'start':
    print('='*60)
    print()

    menu = 'JhonDabe Bank'
    print(menu.center(60, ' '))
    print() 
    print('='*60)
    print()


    while opercao == 0:
        saque = input("What's value saq: ")
        if saque.isdigit():
            opercao = 1
            valor = int(saque)           
            

        else:
            print('Opção inválida !')
            valor = -1
            
        while valor != -1:

            if valor >= ced:                  
                valor -= ced
                total_ced += 1
        
            else:
                if total_ced > 0:
                    print(f'Total de {total_ced} cédulas de {ced}')
                
                if ced == 50:                   
                    ced = 20
                    total_ced = 0

                elif ced == 20:                     
                    ced = 10
                    total_ced = 0
                
                elif ced == 10:                      
                    ced = 1
                    total_ced = 0

                if valor == 0:                    
                    valor = -1
                    opercao = 1
                    inicio = 'stop'

        
   

print('The End !')
 
