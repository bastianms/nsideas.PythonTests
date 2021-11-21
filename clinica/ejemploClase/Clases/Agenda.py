class Agenda:
    def __init__(self):
        self.__personas = []

    def AgregarPersona(self, persona):
        self.__personas.append(persona)

    def MostrarMisContactos(self):
        for persona in self.__personas:
            persona.mostrar()
    
    def BuscarPorEmail(self, email):
        for persona in self.__personas:
            if persona.email == email:
                persona.mostrar()
    
    def EliminarPorEmail(self, email):
        index = 0
        for persona in self.__personas:
            if persona.email == email:
                self.__personas.pop(index)
            index = index + 1