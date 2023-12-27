dic = {}
client = True
while True:
    if client:
        x = input('name ')
        client = False
        dic[x] = {}

    print(dic)

    a = input('Key ')
    b = input('valor ')

    dic[x].update( {a: b} )
    print(dic)

    new_client = input('novo ')
    if new_client in 'yY':
        client = True