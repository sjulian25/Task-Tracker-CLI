import datetime,json,os

from tareas import *

ruta_base = os.path.dirname(__file__)
ARCHIVO_JSON = os.path.join(ruta_base,'archivo_json.json')
tareas=[]
def agregar_tarea():
    try:
        with open(ARCHIVO_JSON,'r') as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        tareas = []

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
    guardar_json(tareas)
    
def guardar_json(tareas):
    with open(ARCHIVO_JSON,'w') as archivo:
        json.dump(tareas,archivo,indent=4)
        print('Cambio guardao con exito')

    

def mostrar():
    with open(ARCHIVO_JSON,'r') as archivo:
        actividad = json.load(archivo)

    for i in actividad:
        print(f"Id: {i['Id']}\nDescripcion: {i['Descripcion']}\nFecha: {i['Fecha']}\nEstado: {i['Estado']}\nModificacion: {i['Modificacion']}")
        print('*'*35)

def cambia_estado():
    id = input('Ingrese el ID de la tarea')
    with open(ARCHIVO_JSON,'r') as archivo:
        tareas = json.load(archivo)

    encontrado=False

    for i in tareas:
        if i['Id']== id:
            i['Estado'] = 'Terminado'
            print(i['Estado'])
            encontrado = True

    if encontrado:
        guardar_json(tareas)
    else:
        print('No se encontrado la tarea con Id:{id}')
        
    
    
    





