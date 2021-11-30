
# Conexion con la base de datos
conexion = mysql.connector.connect(
    host = 'db', # en la situacion de tener el servidor localmente, es localhost
    port = '3306',
    user = 'root',
    password = 'masterdba',
    database = 'pythontest'
)

# Crear cursor para operar sobre la base de datos
cursor = conexion.cursor()

# Ejecutar consultas sobre la base de datos mediante el cursor
cursor.execute("SELECT * FROM usuario")
# Recuperar el resultado de la consulta ejecutada en la linea anterior
resultado = cursor.fetchall()

print(resultado)

# Cerrar la conexion con la base de datos
conexion.close()