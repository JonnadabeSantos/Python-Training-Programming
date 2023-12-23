class ShoppingCart:
    def __init__(self):
        self.__products = []

    def insert_product( self, buy ):
        self.__products.append( buy )
    
    def list_shoppingCart( self ):
        for product in self.__products:
            print( f'{product.name} - {product.valor}' )

class BuyProduct:
    list_products = {1:[ 'Glasses', 12.25 ], 
                     2:[ 'T-shirt', 15 ], 
                     3:[ 'Shoes', 26.21 ], 
                     4:[ 'Clock', 41.11 ],
                     5:[ 'SmartPhone', 1524.24 ],
                     6:[ 'SmartTV', 2415.35 ],
                     7:[ 'Notebook', 3524.95 ],
                     8:[ 'Ball', 24 ],
                     9:[ 'Headphones', 45 ],
                     10:[ 'Printer', 658 ],
                     11:[ 'Mouse', 36.25 ],
                     12:[ 'Kayboard', 25 ],
                     13:[ 'Chair', 215.36 ],
                     14:[ 'Air Fryer', 345 ],
                     15:[ 'Drill', 419.71 ]
                     }


    def __init__( self, name, valor ):
        self.name = name
        self.valor = valor