from usuario.Usuario import Usuario
from usuario.UsuarioRepositorio import UsuarioRepositorio

pablo = Usuario()
pablo.email = 'pablo@sucorreo.cl'
pablo.password = b'qwerty'

repositorioUsuario = UsuarioRepositorio()
# repositorioUsuario.CrearUsuario(pablo)

usuarioPrueba = repositorioUsuario.ObtenerUsuarioPorEmail('pablo@sucorreo.cl')
print(usuarioPrueba.id)

print(repositorioUsuario.ValidarPassword('pablo@sucorreo.cl', b'qwerty'))