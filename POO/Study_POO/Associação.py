class Escritor:
    def __init__( self, name ):
        self.__name = name
        self.__ferramenta = None # VAZIO para receber qualquer tipo de info.

    @property
    def nome( self ):
        return self.__name
    
    @property
    def ferramenta( self ):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta( self, ferramenta ):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__( self, marca):
        self.__marca = marca
    
    @property
    def Caneta( self, marca ):
        self.__marca = marca

    def escrever( self ):
        print( 'Caneta está escrevendo...' )