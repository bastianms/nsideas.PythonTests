# importar lobreria para conectarme con una base de datos mysql
import mysql.connector

# Estructura con parametros de conexion
crendenciales = {
    'host': 'localhost',
    'user': 'root',
    'password': 'masterdba',
    'database': 'clinicapoo'
}

# Entablar conexion con base de datos
conexion = mysql.connector.connect(**crendenciales)

# Establecer el cursor para realizar operaciones
cursor = conexion.cursor()

# Ejecutar un select en la tabla prueba
cursor.execute("SELECT * FROM prueba")
# Recuperar los datos de la consulta
resultado = cursor.fetchall()
print(resultado)

# Mostrar resultado con un ciclo for
for registro in resultado:
    print('Id:', registro[0],', Nombre:', registro[1])

conexion.close()