from datetime import datetime
from colorama import Fore, init
import json
import os
init(autoreset=True)

archivo_json = os.path.join(os.path.dirname(__file__), "tareas.json")

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
            estado = v.get("estado", "No definido")
            fecha = v.get("fecha", "No definida")
            print(f"{i}. {k} - Estado: {estado}, Fecha: {fecha} ")


def Iniciar():
    Opcion = int(input("Digite el numero segun la opcion que desea usar "))
    if Opcion >=1 and Opcion <=5:
        match Opcion:
            case 1:
                AddTarea = input("Agregue una nueva tarea ")
                fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
                Tarea[AddTarea] = {"estado": "pendiente", "Fecha":fecha_actual}
                guardar_tareas()
                print(Fore.GREEN + "✅ Tarea agregada con éxito.")
                MostrarTareas()
            case 2:  
                MostrarTareas()
                clave_antigua = input("Escribe la tarea que quieres actualizar ")
                if clave_antigua in Tarea:
                    clave_nueva = input("Escribre la nueva tarea ")
                    valor_nuevo =  input("Marca la nueva tarea 'en proceso' o 'Terminada' ")
                    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
                    Tarea[clave_nueva] = {"estado": valor_nuevo, "fecha":fecha_actual}
                    del Tarea[clave_antigua]
                    guardar_tareas()
                    print(Fore.GREEN +  "✅ Tarea actualizada con éxito.")
                else:
                    print(Fore.RED + "❌ No se encontró la tarea.")
            case 3:
                MostrarTareas()
                remover = input("Ingrese ")
                del Tarea[remover]
                guardar_tareas()
                print(Fore.GREEN + "✅ Tarea eliminada con éxito.")
            case 4:
                MostrarTareas()
                tarea = input("Escriba la tarea que desea marcar como 'en proceso' o 'terminada' ")
                if tarea in Tarea:
                    estado = input("Escriba 'en proceso' o 'Terminada'")
                    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
                    Tarea[tarea] = {"estado":estado, "fecha": fecha_actual}
                    guardar_tareas()
                    print(Fore.GREEN + "✅ Estado actualizado con éxito.")
                else:
                    print(Fore.RED + "❌ No se encontró la tarea.")
            case 5:
                MostrarTareas()
    else:
        print(Fore.RED + "❌ Dijite un numero valido")
    Iniciar()

def Pregunta():
    Start = input("Digite Start Para Iniciar ")
    if Start == "Start":
        Opciones()
        Iniciar()
    else:
        print(Fore.RED + "❌ Digita 'Start'")
        Pregunta()


