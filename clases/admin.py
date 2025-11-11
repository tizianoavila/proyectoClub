class Administrador():
    def __init__(self, nombre, usuario, contrasena):
        self.nombre = nombre
        self.__usuario = usuario
        self.__contrasena = contrasena
        
    #usuario
    def get_usuario(self):
        return self.__usuario
    def set_usuario(self):
        return self.__usuario
    
    #contraseña
    def get_contraseña(self):
        return self.__contrasena
    def set_contraseña(self):
        return self.__contraseña