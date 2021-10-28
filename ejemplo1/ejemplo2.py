import pymysql

class MySQLDataBase:
    def __init__(self, host, username, password, database_name) -> None:
        self.__host = host
        self.__username = username
        self.__password = password
        self.__database_name = database_name
        self.__connection = None
        self.__cursor = None

    def Open(self):
        self.__connection = pymysql.connect(
            host=self.__host,
            user=self.__username,
            database=self.__database_name,
            password=self.__password
        )
        self.__cursor = self.__connection.cursor()
        print('Conexion exitosa.')
    
    def Close(self):
        self.__connection.close()
        print('Conexion con base de datos cerrada.')

    def fetchAll(self, sql):
        try:
            self.__cursor.execute(sql)
            datos = self.__cursor.fetchall()
            return datos
        except Exception as e:
            raise


connMySQL = MySQLDataBase('db', 'root', 'masterdba', 'hr')
connMySQL.Open()
countries = connMySQL.fetchAll('SELECT country_id, country_name FROM countries')
for item in countries:
    print('ID:', item[0], ', Nombre:', item[1])
connMySQL.Close()