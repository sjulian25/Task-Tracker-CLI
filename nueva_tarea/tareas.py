import uuid
from datetime import datetime
class Tareas:
    def __init__(self,nombre):
        self.__fecha = datetime.now().strftime('%Y/%m/%d %H:%M')
        self.__nombre = nombre
        self.estado = 'pendiente'
        self.id = str(uuid.uuid4())[:8]
        self.modificacion = self.__fecha
    
    def getfecha(self):
        return self.__fecha
    def getid(self):
        return self.id
    def getestados(self):
        return self.estado
    def getmodificacion(self):
        return self.modificacion
    def getdescripcion(self):
        return self.__nombre
    def setmodificacion(self):
        self.modificacion= datetime.now().strftime('%Y/%m/%d %H:%M')
    def setestado(self,id):
        self.estado=estado

