# El concepto de variables miembro o variables en general
# tienen que ver con los ambitos de las variables.
# Por una parte, las variables miembro tendran su alcance
# dentro de la clase y durante todo su ciclo de vida.
# Se pueden abrir en miebros de clase y mimebros de objeto.
# Para entender las podriamos comparar con las variables locales
# que seran definidas por ejemplo en un metodo y su alcance existira
# solamente en ese bloque.

class ContadorPersona:
    contador = 0 # variable miembro (de objeto), tiene su alcance dentro de la clase
    titulo = 'Contador de personas' # variable miembro (de clase), tiene su alcance dentro de la clase

    def __init__(self, valorInicial) -> None:
        self.contador = valorInicial # Valor moficado en el constructor y su alcance es dentro del objeto

    def sumaruno(self):
        self.contador = self.contador + 1 # Modificar variable miembro

    def total(self):
        return self.contador # Informar variable miembro

    def proyectarContador(self, valor):
        contador = self.contador + valor # Definir variable local (contador es local, self.contador es una variable de la clase)
        return contador


cont1 = ContadorPersona(0) # Instancia de objeto
cont1.sumaruno()
print('Total contador 1:', cont1.total())
cont1.sumaruno()
print('Total contador 1:', cont1.total())

cont2 = ContadorPersona(4) # Instancia de objeto
cont2.sumaruno()
print('Total contador 2:', cont2.total())
print('Total contador 1:', cont1.total()) # Se puede apreciar que el valor del cont1 no cambia, pues su alcance es de objeto
cont2.sumaruno()
print('Total contador 2:', cont2.total())
print('Total contador 1:', cont1.total()) # Se puede apreciar que el valor del cont1 no cambia, pues su alcance es de objeto

print(cont1.titulo) # Muestra titulo de cont1
print(cont2.titulo) # Muestra titulo de cont2
ContadorPersona.titulo = 'Contador' # Se modifica titulo a nivel de clase
print(cont1.titulo) # Muestra titulo de cont1
print(cont2.titulo) # Muestra titulo de cont2