class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produto( self ):
        print( self.produtos.produto )
        for produto in self.produtos:
            print( produto.nome, produto.valor )
    
    def soma_total( self ):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompra()

p1 = Produto( 'Camiseta', 50 )
p2 = Produto( 'IPhone', 10000 )
p3 = Produto( 'Caneca', 15 )

carrinho.inserir_produtos( p1 )
carrinho.inserir_produtos( p2 )
carrinho.inserir_produtos( p3 )

carrinho.lista_produto()
print( carrinho.soma_total() )
