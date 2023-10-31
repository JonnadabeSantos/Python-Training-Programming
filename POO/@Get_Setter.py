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
                
            print(valid, len( valid ) )
            for ind, select in enumerate( valid ):
                if len( valid ) == 2:
                    if ind == 0:
                        n1 = select * 10
                    
                    else:
                        n2 = select
                        value = n1 + n2

                elif len( valid ) == 3:
                    if ind == 0:
                        n1 = select * 100

                    elif ind == 1:
                        n2 = select * 10
                    
                    else:
                        n3 = select 
                        value = n1 + n2 + n3
            
            valid.clear()
                    
        self._buy = value



                            




x = Product( 'T-shit', 'R%*95 %6*' )
x.discount( 15 )
print( x.buy )

# print( x.discount( 15 ) )