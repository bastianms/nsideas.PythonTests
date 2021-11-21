from Clases.Persona import Persona
from Clases.Agenda import Agenda

manuel = Persona("Manuel", "Rojas", "manuel@sucorreo.cl") #Instanciar un objeto
manuel.apellidos = "Rojas Olivares"
manuel.edad = 10
manuel.mostrar()
manuel.caminar(29)
manuel.caminar(50)

print('Crear agenda y agregar contacto')
miagenda = Agenda()
miagenda.AgregarPersona(manuel)
miagenda.MostrarMisContactos()

print('Agregar nuevo contacto a la agenda')
pablo = Persona("Pablo", "Godoy", "pablo@sucorreo.cl")
miagenda.AgregarPersona(pablo)
miagenda.MostrarMisContactos()

print('Buscar contacto por email: manuel@sucorreo.cl')
miagenda.BuscarPorEmail("manuel@sucorreo.cl")

print('Elminar contacto por su email: manuel@sucorreo.cl')
miagenda.EliminarPorEmail("manuel@sucorreo.cl")

print('Mostrar contenido de la agenda')
miagenda.MostrarMisContactos()

print('Este es mi programa principal')