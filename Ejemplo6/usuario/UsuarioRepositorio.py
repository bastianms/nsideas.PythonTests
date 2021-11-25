from usuario.Usuario import Usuario
from infraestructure.DataBase import DataBase
from Crypto.Hash import MD5

class UsuarioRepositorio:
    def CrearUsuario(self, usuario: Usuario):
        database = DataBase()
        database.Open()
        database.excuteQuery(f"INSERT INTO usuario (email, password) VALUES ('{usuario.email}', '{usuario.password}')")
        database.Close()

    def ModificarUsuario(self, id, usuario: Usuario):
        database = DataBase()
        database.Open()
        database.excuteQuery(f"UPDATE usuario SET email = '{usuario.email}', password = '{usuario.password}' WHERE id = {id}")
        database.Close()
    
    def ObtenerUsuarioPorEmail(self, email) -> Usuario:
        database = DataBase()
        database.Open()
        resultado = database.fetchOne(f"SELECT id, email, password FROM usuario WHERE email = '{email}'")
        usuario = Usuario()
        usuario.id = resultado[0]
        usuario.email = resultado[1]
        usuario.password = ''
        return usuario

    def ValidarPassword(self, email, password): 
        database = DataBase()
        database.Open()
        resultado = database.fetchOne(f"SELECT password FROM usuario WHERE email = '{email}'")
        hash = MD5.new(password)
        PasswordTemporal = hash.hexdigest()
        if PasswordTemporal == resultado[0]:
            return True
        return False