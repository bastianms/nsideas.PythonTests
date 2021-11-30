from basedato.ConexionMySQL import ConexionMySQL

def ConsultarUsuario():
    # Objeto conexion
    conexion = ConexionMySQL()
    # Crear cursor para operar sobre la base de datos
    cursor = conexion.getConexion().cursor()

    # Ejecutar consultas sobre la base de datos mediante el cursor
    cursor.execute("SELECT * FROM usuario")
    # Recuperar el resultado de la consulta ejecutada en la linea anterior
    resultado = cursor.fetchall()

    print(resultado)

    # Cerrar la conexion con la base de datos
    conexion.closeConexion()