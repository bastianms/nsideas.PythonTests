import mysql.connector
from decouple import config

class DataBase:
    def __init__(self, host = config('host'), username = config('username'), password = config('password'), database_name = config('database_name')) -> None:
        self.__host = host
        self.__username = username
        self.__password = password
        self.__database_name = database_name
        self.__connection = None
        self.__cursor = None
        print(host)

    def Open(self):
        self.__connection = mysql.connector.connect(
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

    def fetchOne(self, sql):
        try:
            self.__cursor.execute(sql)
            datos = self.__cursor.fetchone()
            return datos
        except Exception as e:
            raise
    
    def excuteQuery(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__connection.commit()
        except:        
            raise