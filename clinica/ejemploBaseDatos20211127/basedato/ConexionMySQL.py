import mysql.connector
from mysql.connector import errorcode

class ConexionMySQL:
    def __init__(self) -> None:
        self.host = 'db' # en la situacion de tener el servidor localmente, es localhost
        self.port = '3306'
        self.user = 'root'
        self.password = 'masterdba'
        self.database = 'pythontest'
        self.__mydb = None

    def crearConexion(self):
        try:
            self.__mydb = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print('Conexion establecida.')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Usuario o contrasena incorrectas.')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('La base de datos no existe.')
            else:
                print(err)

    def getConexion(self):
        if self.__mydb is None: 
            self.crearConexion()
        return self.__mydb
    
    def closeConexion(self):
        if self.__mydb != None:
            self.__mydb.close()
        self.__mydb = None
        print('Conexion cerrada.')


# Crear cursor para operar sobre la base de datos
# cursor = conexion.cursor()

# Ejecutar consultas sobre la base de datos mediante el cursor
# cursor.execute("SELECT * FROM usuario")
# Recuperar el resultado de la consulta ejecutada en la linea anterior
# resultado = cursor.fetchall()

# print(resultado)

# Cerrar la conexion con la base de datos
# conexion.close()