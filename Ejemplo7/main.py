from flask import Flask
from usuario.UsuarioRepositorio import UsuarioRepositorio

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hola mundo!!!!"

@app.route("/test")
def ruta_test():
    return "Este es mi ruta de test"

@app.route("/hola/<name>")
def saludo(name):
    return f"Hola, {name}"

@app.route("/usuario/<email>")
def usuarioPorEmail(email):
    repositorio = UsuarioRepositorio()
    usuario = repositorio.ObtenerUsuarioPorEmail(email)
    if usuario:
        return {
            "id": usuario.id,
            "email": usuario.email
        }
    return 'No hay usuarios.'