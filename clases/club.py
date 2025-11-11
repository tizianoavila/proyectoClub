class Club: 
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion, socios):
        self.nombre = nombre
        self.descripcion = descripcion 
        self.ubicacion = ubicacion  
        self.__presidente = presidente 
        self.__fecha_fundacion = fecha_fundacion   
        self.actividades = []
        self.__socios = socios   

    def mostrar_info (self):
        print("nombre del club: ", self.nombre)
        print("descripcion: ", self.descripcion)
        print("ubicacion: ", self.ubicacion)
        print("presidente: ", self.__presidente)
        print("fundacion: ", self.__fecha_fundacion)
        
    #presidente
    def get_presidente(self):
        return self.__presidente
    def set_presidente(self):
        return self.__presidente

    #fundacion
    def get_fundacion(self):
        return self.__fecha_fundacion
    def set_fundacion(self):
        return self.__fecha_fundacion
    
    #socios
    def get_fundacion(self):
        return self.__socios
    def set_fundacion(self):
        return self.__socios