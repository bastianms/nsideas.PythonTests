from common.MySQLDataBase import MySQLDataBase

connMySQL = MySQLDataBase('db', 'root', 'masterdba', 'hr')
connMySQL.Open()
countries = connMySQL.fetchAll('SELECT country_id, country_name FROM countries')
for item in countries:
    print('ID:', item[0], ', Nombre:', item[1])
country = connMySQL.fetchOne("SELECT country_id, country_name FROM countries WHERE country_id = 'AR'")
print('ID:', country[0], ', Nombre:', country[1])
#connMySQL.excuteQuery("INSERT INTO countries (country_id, country_name, region_id) VALUES ('CP', 'Copiapo', '2')")
#connMySQL.excuteQuery("UPDATE countries SET country_name = 'Atacama' WHERE country_id = 'CP'")
connMySQL.excuteQuery("DELETE FROM countries WHERE country_id = 'CP'")
connMySQL.Close()
