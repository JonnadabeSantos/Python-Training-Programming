from Buy_list import *

list = BuyProduct.list_products

while True:
    for key, val in list.items():
        if key < 10:
            print( f'0{key} - {val[0]:<15} R$ {val[1]}' )
        else:
            print( f'{key:<2} - {val[0]:<15} R$ {val[1]}' )

    try:
        product = int( input( '\nSelect the product: ' ) )
    except:
        print( 'Number Invalid!' )
    else:
        
        print( f'You selected {list[product] [0]}')
        while True:
    
            try:
                price = float( input( '\nPay the price: ' ) )
            except:
                print( 'Number Invalid!' )
            else:
                if price == list[product] [1]:
                    print( 'Product added successfully' )
                    new_purchase = input( 'Do you want to make a new purchase [Y/N]?: ' )
                    
                    if new_purchase in 'YyNn':
                        break
                else:
                    print( 'Incorrect Value!' )
                
    if new_purchase in 'Nn':
        break