from database.Countries import Countries

country = Countries()

#country.create('CP', 'Copiapo', '2')
print(country.findOne('CP'))
print(country.find())