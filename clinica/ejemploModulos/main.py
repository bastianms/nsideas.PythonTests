from utils.MyException import MyException

class TipoMensaje:
    def __init__(self):
        self.tipo = ""



def MetodoPrueba(tipo_mensaje: TipoMensaje):
    try:
        if tipo_mensaje.tipo == "H":
            print("Hola desde el metodo de prueba")
        elif tipo_mensaje.tipo == "C":
            print("Chao desde el metodo de prueba")
        else:
            raise MyException(tipo_mensaje, "El parametro utilizado no es valido")
    except MyException as ex:
        print(ex)



tipom = TipoMensaje()
tipom.tipo = "Z"

MetodoPrueba(tipom)

