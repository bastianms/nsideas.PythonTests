class clase1:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

class clase2:
    def __init__(self, atributo3, atributo4):
        self.atributo3 = atributo3
        self.atributo4 = atributo4



class todo(clase1,clase2):
    def __init__(self, atributo1, atributo2, atribute3, atributo4):
        clase1.__init__(self, atributo1, atributo2)
        clase2.__init__(self, atribute3, atributo4)
    
    def mostrar(self):
        return f"{self.atributo1} {self.atributo2} {self.atributo3} {self.atributo4}"



objeto = todo("1","2","3","4")
print(objeto.mostrar())