class Agenda:
    def __init__(self):
        self.__personas = []

    def AgregarPersona(self, persona):
        self.__personas.append(persona)

    def MostrarMisContactos(self):
        print(self.__personas)