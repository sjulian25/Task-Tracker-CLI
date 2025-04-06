from datetime import datetime
import json
import os

archivo_json = "tareas.json"

if os.path.exists(archivo_json):
    with open(archivo_json, "r") as archivo:
        Tarea = json.load(archivo)
else:
    Tarea = {}

def guardar_tareas():
    with open(archivo_json, "w") as archivo:
        json.dump(Tarea, archivo, indent=4)

def Opciones():
    print("Bienvenido al Programa\n"
            "Digite el Numero segun lo que desea\n"
            "1. Agregar Tarea\n 2. Actualizar Tarea\n 3. Eliminar Tarea\n 4. Marcar Tarea 'en proceso' o 'Terminada'\n 5.Mostrar Tarea")

def MostrarTareas():
    if not Tarea:
        print("No hay tareas disponibles.")
    else:
        print("Tareas disponibles:")
        for i,(k, v) in enumerate(Tarea.items(), start=1):
            print(f"{1}, {k}: {v}")


def Iniciar():
    Opcion = int(input("Digite el numero segun la opcion que desea usar "))
    match Opcion:
        case 1:
            AddTarea = input("Agregue una nueva tarea ")
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
            Tarea[AddTarea] = None
            Tarea[fecha_actual] = AddTarea
            guardar_tareas()
            print("exito", "Tarea agregada con éxito.")
        case 2:  
            MostrarTareas()
            clave_antigua = input("Escribe la tarea que quieres actualizar ")
            if clave_antigua in Tarea:
                clave_nueva = input("Escribre la nueva tarea ")
                valor_nuevo =  input("Marca la nueva tarea 'en proceso' o 'Terminada' ")
                fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
                Tarea[clave_nueva] = valor_nuevo
                del Tarea[clave_antigua]
                guardar_tareas()
                print("exito", "Tarea actualizada con éxito.")
            else:
                print("error", "No se encontró la tarea.")
        case 3:
            MostrarTareas()
            remover = input("Ingrese ")
            del Tarea[remover]
            guardar_tareas()
            print("exito", "Tarea eliminada con éxito.")
        case 4:
            MostrarTareas()
            tarea = input("Escriba la tarea que desea marcar como 'en proceso' o 'terminada' ")
            if tarea in Tarea:
                estado = input("Escriva 'en proceso' o 'Terminada'")
                Tarea[tarea] = estado
                guardar_tareas()
                print("exito", "Estado actualizado con éxito.")
            else:
                print("error", "No se encontró la tarea.")
        case 5:
            MostrarTareas()
    Iniciar()

def Pregunta():
    Start = input("Digite Start Para Iniciar ")
    if Start == "Start":
        Opciones()
        Iniciar()
    else:
        print("Digita 'Start'")
        Pregunta()


