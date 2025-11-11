class Cuota():
    def __init__(self, estado, fechaVencimiento, periodo):
        self.__estado = estado
        self.fechaVencimiento = fechaVencimiento
        self.periodo = periodo
        
    #cuota
    def get_cuota(self):
        return self.__cuota
    def set_cuota(self):
        return self.__cuota