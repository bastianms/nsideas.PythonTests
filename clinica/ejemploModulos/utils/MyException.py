class MyException(Exception):
    def __init__(self, objeto, mensaje):
        super().__init__("{}. El parametro tipo es invalido en el objeto: {}".format(mensaje, objeto))