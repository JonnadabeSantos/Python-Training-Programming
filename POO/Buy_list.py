class ShoppingCart:
    def __init__(self):
        self.products = []

    def insert_product( self, buy ):
        self.products.append( buy )
    
    def list_shoppingCart( self ):
        for product in self.products:
            print( f'{product.name} - {product.valor}' )

class BuyProduct:
    def __init__( self, name, valor ) -> None:
        self.name = name
        self.valor = valor