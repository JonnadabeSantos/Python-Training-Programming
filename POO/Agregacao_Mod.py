from Agragacao import *

carrinho = CarrinhoDeCompra()

p1 = Produto( 'Camiseta', 50 )
p2 = Produto( 'IPhone', 10000 )
p3 = Produto( 'Caneca', 15 )

carrinho.inserir_produtos( p1 )
carrinho.inserir_produtos( p2 )
carrinho.inserir_produtos( p3 )

carrinho.lista_produto()
print( carrinho.soma_total() )