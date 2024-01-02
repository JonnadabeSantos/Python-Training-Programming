class Product:
    def __init__(self, name, buy):
        self.name = name
        self.buy = buy

    def discount(self, percent):
        self.buy = self.buy - ( self.buy * ( percent / 100 ) )

    def increase( self, percent ):
        self.buy = self.buy = ( self.buy * ( percent / 100 ) )

    @property
    def buy( self ):
        return self._buy
    
    @buy.setter
    def buy ( self, value ):
        if isinstance( value, str ):
            #value = float( value.replace( 'R$', '' ) )
           
            # My Aplication !
            valid = []
            for number in value:
                if number.isdigit():
                    valid.append( float( number ) )
                    print(f'{number} is number valid !')

            cont = value = 0
            cont = len( valid )

            for ind, select in enumerate( valid ):

                if ind == 0 or cont != 1:
                    cont -= 1
                    value += select * ( 10 ** cont )

                else:
                    value += select
                    print(f'Total {value:.2f} R$')
           
            valid.clear()
                    
        self._buy = value   


x = Product( 'T-shit', '6R1%*5 %6*0' )
x.discount( 15 )
print( x.buy )

# print( x.discount( 15 ) )