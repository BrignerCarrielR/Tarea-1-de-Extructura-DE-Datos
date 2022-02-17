import os, time

def cls():
    os.system("cls")

def msg(ind):
    if ind == 3:
        print("Ingrese sólo caracteres...")
    if ind == 2:
        print("Ingrese un dato válido")
    elif ind == 1:
        input("\nPresione una tecla para salir...")
        cls()
    elif ind == 0:
        print("Ingrese sólo valores numéricos...")

def ValidarNum(inf):
        print(inf)
        while True:
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                msg(0)
                time.sleep(1)
                print(" "*33)
        return int(valor)