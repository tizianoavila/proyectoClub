from club import Club

class clubInferiores(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion, socios):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion, socios)
        
        