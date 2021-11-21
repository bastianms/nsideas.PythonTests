class Persona:
    def __init__(self, nombre, apellidos, email): #Constructor de la clase
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.__edad = 0
        self.__pasos = 0

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self.__edad = valor
        else:
            print('La edad ingresada no es valida')

    def mostrar(self):
        print("Nombre:", self.nombre, ", Apellidos:", self.apellidos, ", email:", self.email, ", edad:", self.edad)

    def caminar(self, pasos):
        self.__pasos = self.__pasos + pasos
        print("Haz dado", self.__pasos,"pasos.")