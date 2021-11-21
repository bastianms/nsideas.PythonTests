from Clases.Persona import Persona
from Clases.Agenda import Agenda

manuel = Persona("Manuel", "Rojas", "manuel@sucorre.cl") #Instanciar un objeto
manuel.apellidos = "Rojas Olivares"
manuel.edad = 10
manuel.mostrar()
manuel.caminar(29)
manuel.caminar(50)

miagenda = Agenda()
miagenda.MostrarMisContactos()
miagenda.AgregarPersona(manuel)
miagenda.MostrarMisContactos()

print('Este es mi programa principal')