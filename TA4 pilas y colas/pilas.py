class Pilas:                
    def __init__(self,tamanio=0):
        self.lista=[]
        self.tope=0
        self.size=tamanio
     
    def empty(self):
        return self.tope == 0
    
    def ppush(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Pila está Llena")
    def tamanio(self):
        return self.size == 0
    def Ppop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            print("Dato Eliminado:",top)
            return top
            
    def Llongitud(self):
        return self.tope
        
    def Sshow(self):
        if self.empty():
            print("*"*20,"Lista Vacia","*"*20)
        else:
            print("*"*20,"Lista de Datos","*"*20)                    
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope]))    
    
    def Bbuscar(self,buscado):
        print("La posicion del dato buscado es: ",self.lista.index(buscado))
   
# pila = Stack(5)
# pila.push("4")       
# pila.push("3")       
# pila.push("2")       
# pila.push("5")       
# pila.push("20")       
# pila.push("10")   
# pila.show()    
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
