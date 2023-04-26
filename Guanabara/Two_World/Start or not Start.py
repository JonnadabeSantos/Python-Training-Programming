city = str( input('Digite sua Cidade: ').lower() ).strip() .split()
# city = city.split()
print(city,'\n')

#===========================================================================
condition = 'inicia com' if 'santos' in city[0] else 'Não tem inicia com'
#===========================================================================

print('Sua cidade {} santos'.format(condition))