from Buy_list import *

list = BuyProduct.list_products
client = True
confirmed_purchase = {}

while True:
    for key, val in list.items():
        #I just wanted to test my formatting skills
        list[key] [1] = float( list[key] [1] ) # Add decimals ( .0 )
        list[key] [1] = str( list[key] [1] )
        if '.0' in list[key] [1]:
            list[key] [1] = list[key] [1].replace('.0','.00')

        if key < 10:        
            print( f'0{key} - {val[0]:<15} R$ {val[1].replace('.',',')}' )
        else:           
            print( f'{key:<2} - {val[0]:<15} R$ {val[1].replace('.',',')}' )

        list[key] [1] = float( list[key] [1] ) # returns the original value

    if client:
        new_client = input( '\nType client name: ')
        confirmed_purchase[new_client] = {}
        client = False
        print( confirmed_purchase )

    try:
        product = int( input( '\nSelect the product: ' ) )
    except:
        print( 'Number Invalid!' )
    else:
        
        print( f'You selected {list[product] [0]}' )
        while True:
    
            try:
                price = input( '\nPay the price: ' )
                if ',' in price:
                    price = price.replace( ',', '.' )
                price = float( price )
                print( price )

            except:
                print( 'Number Invalid!' )
            else:
                if price == list[product] [1]:
                    buy = BuyProduct( list[product] [0], price )

                    confirmed_purchase[new_client].update( {buy.name: buy.valor} )
                    print( confirmed_purchase )
                    print( 'Product added successfully' )
                    new_purchase = input( 'Do you want to make a new purchase [Y/N]?: ' )
                    
                    if new_purchase in 'YyNn':
                        break
                else:
                    print( 'Incorrect Value!' )
                
    if new_purchase in 'Nn':
        break


print(confirmed_purchase)