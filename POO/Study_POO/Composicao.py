class Cliente:
    def __init__( self, nome, idade ) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco( self, cidade, estado ):
        self.enderecos.append( Endereco( cidade, estado ) ) # append recebe um objeto ( a class ), Endereco necessita instanciar 2 atributos, por isso append parece ter "recebido" mais de um "atributo" 

    def lista_enderecos( self ):
        for endereco in self.enderecos:
            print( endereco.cidade, endereco.estado ) # ^>

    def __del__( self ):
        print( f'{self.nome} FOI APAGADO' )


class Endereco:
    def __init__( self, cidade, estado ):
        self.cidade = cidade # ^>
        self.estado = estado # ^>
     
    def __del__( self ):
        print( f'{self.cidade}/{self.estado} FOI APAGADO...')



        

c2 = Cliente( 'Luiz', 32 )
print( c2.nome )
c2.insere_endereco( 'Belo Horizonte', 'MG' )
c2.lista_enderecos()
del c2
print()

c2 = Cliente( 'Maria', 24 )
print( c2.nome )
c2.insere_endereco( 'Salvador', 'BA' )
c2.insere_endereco( 'Rio de Janeiro', 'RJ' )
c2.lista_enderecos()
del c2
print()

c3 = Cliente( 'João', 19 )
c3.insere_endereco( 'São Paulo', 'SP')
print( c3.nome )
c3.lista_enderecos()
del c3
print()

print( '################################################' )

