# Clase: abstraccion de un objeto (un objeto de la vida real)
class Persona:
    def __init__(self) -> None:
        self.email = ""
        self.nombre = ""
        self.apellido = ""
        self.__edad = 0 # atributo private

    @property # getter de la propiedad
    def edad(self):
        return self.__edad;
    
    @edad.setter # setter de la propiedad
    def edad(self, valor):
        if valor >= 0:
            self.__edad = valor

    def mostrar(self):
        print(self.email, self.nombre, self.apellido, self.__edad)
    
class Usuario(Persona):
    def mostrar2(self):
        self.edad = 34
        print(self.email, self.edad)
# Objetos: es una instancia de una clase (es la materializacion de un clase en un objeto)
# Instanciar: es la accion de materializar una clase en un objeto
marcelo = Persona()
marcelo.email = "marcelo@suemail.cl"
marcelo.nombre = "Marcelo"
marcelo.apellido = "Rojas"
marcelo.edad = -1
marcelo.mostrar()


pedro = Usuario()
pedro.email = "pedro@sucorre.cl"
if pedro != None:
    pedro.edad = 23
    pedro.mostrar()

