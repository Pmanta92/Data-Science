import os

runPrograma = True # Variable para controlar el bucle
todoLista = [] # Lista para almacenar las tareas

# Funcion para mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("Por favor seleccione una opcion:")
    print("")
    print("")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar tarea")
    print("4. Salir")

# funcion para marcar una tarea como realizada
def updateTodo():
    os.system("cls") # Limpiar la pantalla
    showTodoList()
    global todoLista # Declarar la variable todoLista como global
    print("Actualizar una tarea")
    todoId = int(input("Ingresa el id de la tarea que quiere marcar como hecha: ")) # Pedir al usuario que ingrese el id de la tarea
    todoLista[todoId-1] = todoLista[todoId-1] + " (✓)" # Marcar la tarea como hecha
    os.system("cls") # Limpiar la pantalla
    showTodoList() # Llamar a la función showTodoList para mostrar la lista de tareas

# fun para guardar las tareas en la variable todoLista
def createTodo():
    os.system("cls") # Limpiar la pantalla
    global todoLista # Declarar la variable todoLista como global
    print("Crear una nueva tarea")
    todo = input("Ingresa el nombre de la tarea: ") # Pedir al usuario que ingrese el nombre de la tarea
    todoLista.append(todo) # Agregar la tarea a la lista
    #print("Tarea guardada con exito") # Mensaje de confirmación
    # Mostar la lista de tareas
    showTodoList() # Llamar a la función showTodoList para mostrar la lista de tareas

# funcion para crear una tarea
def showTodoList():
    global todoLista # Declarar la variable todoLista como global
    print("")
    print("")
    print("***************************************************")
    for todo in todoLista:
        print(f"{todoLista.index(todo)+1}. {todo}") # le sumo 1 al indice para que empiece desde 1
    print("***************************************************")
    print("")

# funcion que nos pérmite borrar una tarea
def deleteTodo():
    os.system("cls") # Limpiar la pantalla
    showTodoList()
    global todoLista # Declarar la variable todoLista como global
    print("Borrar una tarea")
    todoId = int(input("Ingresa el id de la tarea que quiere borrar: ")) # Pedir al usuario que ingrese el id de la tarea
    del todoLista[todoId-1] # Borrar la tarea de la lista
    os.system("cls") # Limpiar la pantalla
    showTodoList() # Llamar a la función showTodoList para mostrar la lista de tareas
    
def main():
    global runPrograma # Declarar la variable runPrograma como global
    print(".: Bienvenido a PYTHON a Todo List :.")

    while runPrograma:
        showMenuOptions() # Llamar a la función showMenuObtions
        option = int(input("Ingresa el numero de la opcion: "))

        match option:
            case 1:
                createTodo() # Llamar a la función createTodo
            case 2:
                updateTodo() # Llamar a la función updateTodo
            case 3:
                deleteTodo() # Llamar a la función deleteTodo
            case 4:
                os.system("cls") # Limpiar la pantalla
                print("******************** Hasta luego!!! **********************")
                print("************** Gracias por usar el programa ************** \n")
                runPrograma = False # Salir del bucle si la opción no es válida
            case _:
                os.system("cls") # Limpiar la pantalla
                print("********* Opcion no valida, Ingrese una opcion valida *********")
                print("*************** Por favor, vuelva a intentarlo **************** \n")
                runPrograma = False # Salir del bucle si la opción no es válida

if __name__ == "__main__":  #"__name__" es una variable especial que contiene el nombre del módulo actual
    main() # Llamar a la función main si el script se ejecuta directamente