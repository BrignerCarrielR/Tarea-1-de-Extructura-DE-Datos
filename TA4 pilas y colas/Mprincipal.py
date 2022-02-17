import os
from MMenu import Menu
from lista import Lista
from pilas import Pilas
from colas import Colas
from validar import cls, ValidarNum, msg

menupr = Menu()
llamarlista=Lista()
llamarpilas=Pilas()
llamarcolas=Colas()
lista = ["1) Lista","2) Pilas","3) Colas","4) Salir"]
lista1 = ["1) Push","2) Pop","3) Show","4) eliminar","5) insertar","6) buscar","7) Regresar"]
lista2 =["1) Cambiar Tamaño de lista", "2) Push","3) Pop","4) Show","5) buscar","6) longitud","7) Regresar"]
opcion=""

while opcion != "4":
    os.system("cls")
    opcion = menupr.menu(lista,"Menu Principal")
    opc1=""
    if opcion == "1":
        while opc1 != "7":
            os.system("cls")
            opc1 = menupr.menu(lista1,"Menu de Lista")
            os.system("cls")
            
            if opc1 == "1":
                llamarlista.mostrar()
                print("*"*20,"Ingreso de datos","*"*20)
                nuevodato=input("nuevo dato: ")
                llamarlista.push(nuevodato) 
                input("Datos ingresados correctamente, Precione una tecla para continuar.....")
            if opc1 == "2":
                llamarlista.mostrar()
                print ("*"*20,"Eliminar Dato","*"*20)
                llamarlista.pop()
                input("Precione una tecla para continuar.....")
            if opc1 == "3":
                llamarlista.mostrar()
                input("Precione una tecla para continuar.....")
            if opc1 == "4":
                llamarlista.mostrar()
                print ("*"*20,"Eliminar Dato por posicion","*"*20)
                eliminardato=ValidarNum("Ingrese posicion de dato a eliminar: ")
                os.system("cls")
                print ("*"*20,"Eliminar Dato por posicion","*"*20)
                print("Dato elimidado: ",llamarlista.eliminarElemento(eliminardato))
                input("Precione una tecla para continuar.....")
            if opc1 == "5":
                llamarlista.mostrar()
                print("*"*20,"Insertar dato","*"*20)
                inserpos=ValidarNum("Posicion en la que desea insertar : ")
                inserdato=input("Dato que desea insertar : ")
                llamarlista.insertarElemento(inserpos,inserdato)
                os.system("cls")
                print("*"*20,"Insertar dato","*"*20)
                print("Dato insertado correctamente.")
                input("Precione una tecla para continuar.....")
            if opc1 == "6":
                llamarlista.mostrar()
                print("*"*20,"Buscar Dato","*"*20)
                buscardato=input("Ingrese dato para conocer su posicion: ")
                os.system("cls")
                print("*"*20,"Buscar Dato","*"*20)
                llamarlista.buscar(buscardato)
                input("Precione una tecla para continuar.....")
        input("SALIENDO....., presiones una tecla para continuar.")

    elif opcion == "2":
        while opc1 != "7": 
            os.system("cls")
            if llamarpilas.tamanio():
                llamarpilas= Pilas(ValidarNum("Ingrese tamaño de la pila: "))
            os.system("cls")
            opc1 = menupr.menu(lista2,"Menu de Pilas")
            os.system("cls")
            if opc1 == "1":
                llamarpilas = Pilas(ValidarNum("Ingrese el tamaño de la nueva cola: "))
            if opc1 == "2":
                print ("*"*20,"Ingresar Datos","*"*20)
                nota=input("Ingrese valores: ")
                llamarpilas.ppush(nota)
                input("Precione una tecla para continuar.....")
            if opc1 == "3":
                llamarpilas.Sshow()
                print ("*"*20,"Eliminar Dato","*"*20)
                llamarpilas.Ppop()
                input("Precione una tecla para continuar.....")
            if opc1 == "4":
                llamarpilas.Sshow()
                input("Precione una tecla para continuar.....")
            if opc1 == "5":
                llamarpilas.Sshow()
                print("*"*20,"Buscar Dato","*"*20)
                buscardat=input("Ingrese dato para conocer su posicion: ")
                os.system("cls")
                print("*"*20,"Buscar Dato","*"*20)
                llamarpilas.Bbuscar(buscardat)
                input("Precione una tecla para continuar.....")
            if opc1 == "6":
                llamarpilas.Sshow()
                print("El tope de la lista es {}".format(llamarpilas.Llongitud()))
                input("Precione una tecla para continuar.....")

    elif opcion == "3":
        while opc1 != "7":
            os.system("cls")
            if llamarcolas.tamanio():
                llamarcolas= Colas(ValidarNum("Ingrese tamaño de la Cola: "))
            os.system("cls")
            opc1 = menupr.menu(lista2,"Menu de Colas")
            if llamarcolas.tamanio():
                llamarcolas= Colas(ValidarNum("Ingrese tamaño de la Cola: "))
            os.system("cls")
            if opc1 == "1":
                llamarcolas = Colas(ValidarNum("Ingrese el tamaño de la nueva cola: "))
            if opc1 == "2":
                print ("*"*20,"Ingresar Datos","*"*20)
                nota=input("Ingrese valores: ")
                llamarcolas.Cpush(nota)
                input("Precione una tecla para continuar.....")
            if opc1 == "3":
                llamarcolas.Cshow()
                print ("*"*20,"Eliminar Dato","*"*20)
                llamarcolas.Cpop()
                input("Precione una tecla para continuar.....")
            if opc1 == "4":
                llamarcolas.Cshow()
                input("Precione una tecla para continuar.....")
            if opc1 == "5":
                llamarcolas.Cshow()
                print("*"*20,"Buscar Dato","*"*20)
                buscadat=input("Ingrese dato para conocer su posicion: ")
                os.system("cls")
                print("*"*20,"Buscar Dato","*"*20)
                llamarcolas.Cbuscar(buscadat)
                input("Precione una tecla para continuar.....")
            if opc1 == "6":
                llamarcolas.Cshow()
                print("El tope de la lista es {}".format(llamarcolas.Clongitud()))
                input("Precione una tecla para continuar.....")
    elif opcion == "4":
            os.system("cls")
            print("'Salir'")
            print("'Fin de la Ejecución'")
            
    