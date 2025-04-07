from funciones import *

while True:
    mostrar()
    print('Seleccion la opcion que desea realizar\n1. Agregar una nueva tarea\n2. Cambiar el estado de una tarea\n3. Mirar las tareas pendientes\n4. Salir')
    seleccion = int(input('Ingrese la opcion'))

    match seleccion:
        case 1:
            agregar_tarea()
        
        case 2:
            cambia_estado()
        
        case 3:
            eliminar_tareas()


