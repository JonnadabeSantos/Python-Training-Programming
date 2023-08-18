import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except(urllib.error.URLError):
    print('O site Pudim não está acessível! ')
else:
    print('Conseguir acessar o site pudim com sucesso!')
    # print(site.read())