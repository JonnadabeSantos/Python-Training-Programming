from menus import *

class ShoppingCart:
    def __init__(self):
        self.__products = {}

    def insert_product( self,key, name, buy, client=False ):       
        if client:
            self.__products[key] = [ [ name, buy ] ]        
        else:
            self.__products[key].append( [ name, buy ] )
            
        print( self.__products )

    
    def list_shoppingCart( self ):
        cont = 1
        summ = 0
        keyclients = []
        print( cabeçalho( 'Client Select' ) )

        for key in self.__products.keys():
            keyclients.append( key )
            print( f'{ cont } - { key }' )
            cont += 1
        
        select = int( input( '\nSelect purchases by customers: ' ) )
        for key in self.__products.keys():
            if keyclients[select - 1] == key:
                print( cabeçalho( f"These are {key}'s purchases" ) )
                
                for ind, buyed in enumerate( self.__products[ keyclients[ select - 1 ] ] ):                                        
                    summ += buyed[1]
                    price = COMAdecimal( buyed[1] )
                    
                    print( f'{ind + 1}º - {buyed[0]:.<25} R$ {price}' )                    
                
                summ = COMAdecimal ( summ )
                Total_purchased = 'Total purchased'
                print( f'\n{Total_purchased:.<30} R$ {summ}')



class BuyProduct:
    list_products = { 1:[ 'Glasses',    12.25 ], 
                      2:[ 'T-shirt',    15 ], 
                      3:[ 'Shoes',      26.21 ], 
                      4:[ 'Clock',      41.11 ],
                      5:[ 'SmartPhone', 1524.24 ],
                      6:[ 'SmartTV',    2415.35 ],
                      7:[ 'Notebook',   3524.95 ],
                      8:[ 'Ball',       24 ],
                      9:[ 'Headphones', 45 ],
                     10:[ 'Printer',    658 ],
                     11:[ 'Mouse',      36.25 ],
                     12:[ 'Kayboard',   25 ],
                     13:[ 'Chair',      215.36 ],
                     14:[ 'Air Fryer',  345 ],
                     15:[ 'Drill',      419.71 ]
                     }


    def __init__( self, name, valor ):
        self.name = name
        self.valor = valor
        print('cadastrou')
    
    @property
    def valor( self ):
        return self._valor
    
    @valor.setter
    def valor( self, val ):
        if isinstance( val, str ):
            val = float( val )
            print('validou')
            
        self._valor = val
        