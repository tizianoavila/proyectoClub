class Socio:
    def __init__(self, fechaInscripcion, estado, usuario, contrasena):
        self.fechaInscripcion = fechaInscripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contrasena = contrasena
        
    #usuario
    def get_usuario(self):
        return self.__usuario
    def set_usuario(self):
        return self.__usuario
            
    #contraseña
    def get_contraseña(self):
        return self.__contraseña
    def set_contraseña(self):
        return self.__contraseña
            