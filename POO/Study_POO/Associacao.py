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
    def marca( self ):
        return self.__marca

    def escrever( self ):
        print( 'Caneta está escrevendo...' )

class MaquinaDeEscrever:
     def escrever( self ):
         print( 'Máquina está escrevendo' )



escritor = Escritor( 'Joãozinho' )
caneta = Caneta( 'Bic' )
maquina = MaquinaDeEscrever()



escritor.ferramenta = caneta # Associa com tudo quem tem na Classe Caneta
escritor.ferramenta.escrever()
print( 'Escritor >> ', escritor.ferramenta.marca )
print( 'Caneta >>' , caneta.marca )
del escritor

print( 'Caneta ON >>' , caneta.marca )
# escritor.ferramenta = maquina # Associa com tudo quem tem na Classe Maquina
# escritor.ferramenta.escrever()
# print( 'Escritor >> ', escritor.ferramenta.escrever() )

