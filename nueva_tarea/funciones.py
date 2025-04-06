import datetime,json,os

from tareas import *

ruta_base = os.path.dirname(__file__)
ARCHIVO_JSON = os.path.join(ruta_base,'archivo_json.json')
tareas=[]
def agregar_tarea():
    actividad = input('Escriba el nombre de la tarea ')
    compromiso = Tareas(actividad)#agregar el objeto a una base de datos
    tarea = {
        'Id':compromiso.getid(),
        'Descripcion':compromiso.getdescripcion(),
        'Fecha':compromiso.getfecha(),
        'Estado': compromiso.getestados(),
        'Modificacion': compromiso.getmodificacion()
    }
    tareas.append(tarea)
    guardar_json()
    
def guardar_json():
    with open(ARCHIVO_JSON,'w') as archivo:
        json.dump(tareas,archivo,indent=4)
    


""" def cambia_estado():
    id = input('Ingrese el ID de la tarea')
    estado = input('Ingrese el nuevo estado de actividad (completada o pendiente)')
    tareas.getestado(estado,id) """


