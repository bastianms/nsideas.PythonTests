import pymysql


class MySQLDataBase:
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host='db',
            user='root',
            password='masterdba',
            db='demo'
        )
        self.connection.cursor()
        print('Conexion correcta.')

    def prueba(self):
        return 'prueba'

    #sql = 'SELECT {}'.format(id)
    #try:
    #self.cursor.execute(sql)
    #user = self.cursor.fetchone()
    #user = self.cursor.fetchall ()
    #self.connection.commit()
    #self.connection.close()
    #except Exception as e:
    #raise


database = MySQLDataBase()
