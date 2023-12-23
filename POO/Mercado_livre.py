from Buy_list import *

list = BuyProduct.list_products


for key, val in list.items():
    if key < 9:
        print( f'0{ key:.2f } - { val[0] } R$ { val[1] }' )
    else:
        print( f'{ key:<2f } - { val[0] } R$ { val[1] }' )

# while True:
#     # product = input( '')