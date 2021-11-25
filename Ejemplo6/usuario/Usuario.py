from Crypto.Hash import MD5

class Usuario:
    def __init__(self) -> None:
        self.id = 0
        self.email = ''
        self.__password = ''
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        hash = MD5.new(valor)
        self.__password = hash.hexdigest()

    def mostrar(self):
        return f'{self.id} / {self.email}'