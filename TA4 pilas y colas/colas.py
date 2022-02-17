
class Colas:                
    def __init__(self,tamanio=0):
        self.lista=[]
        self.tope=0
        self.size=tamanio
     
    def empty(self):
        # if self.tope == 0:
        #     return True
        # else:
        #     return False
        return self.tope == 0
    
    def Cpush(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
    def tamanio(self):
        return self.size == 0 
    def Cpop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[0]
            self.tope -= 1
            self.lista = self.lista[1:]
            print("Dato Eliminado:",top)
            return top

    def Clongitud(self):
        return self.tope

    def Cshow(self):
        if self.empty():
            print("Lista vacia")
        else:
            print("*"*20,"Lista de Datos","*"*20)  
            for i in range(0,self.tope):
                print("[{}]".format(self.lista[i]))

    def Cbuscar(self,buscado):
        if buscado in self.lista:
            for pos in range(0,len(self.lista)):
                if buscado == self.lista[pos]:
                    print("La posición es {}".format(pos+1))
        else:
            print("-1")
# pila.push("4")       
# pila.push("3")       
# pila.push("2")       
# pila.push("5")       
# pila.push("20")       
# pila.push("10")   
# pila.buscar()    
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())