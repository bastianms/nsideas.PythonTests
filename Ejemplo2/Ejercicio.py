from mysqlDataBase import MySQLDataBase

connMySQL = MySQLDataBase('db', 'root', 'masterdba', 'hr')
connMySQL.Open()
countries = connMySQL.fetchAll('SELECT country_id, country_name FROM countries')
for item in countries:
    print('ID:', item[0], ', Nombre:', item[1])
connMySQL.Close()
