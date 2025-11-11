class Persona:
    def __init__(self, nombreCompleto, edad, tipoIdentificacion, identificacion, nacionalidad):
        self.nombreCompleto = nombreCompleto
        self.edad = edad
        self.__tipoIdentificacion = tipoIdentificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad
        
    #tipoId
    def get_tipoIdentificacion(self):
        return self.__tipoIdentificacion
    def set_tipoIdentificacion(self):
        return self.__tipoIdentificacion
    
    #identificacion
    def get_identificacion(self):
        return self.__identificacion
    def set_identificacion(self):
        return self.__identificacion
    
    #nacionalidad
    def get_nacionalidad(self):
        return self.__nacionalidad
    def set_nacionalidad(self):
        return self.__nacionalidad
    