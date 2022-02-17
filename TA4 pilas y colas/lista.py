class Lista:
    def __init__(self,datos=["Daniel","Yady","Ana","Jose","Moises"]) -> None:
        self.lista=datos
    
    def push(self,dato):
        self.lista.append(dato)
        
    def pop(self):
        ultimo = self.lista.pop()
        print ("Dato Eliminado:",ultimo)
        return ultimo
    
    def eliminarElemento(self,pos):
        pos = pos-1
        if pos in range(0,len(self.lista)):
            ele = self.lista[pos]     
            self.lista = self.lista[0:pos] + self.lista[pos+1:]
            return ele
        else:
            return None





            #return "Posicion:{} no existe en la lista".format(pos) 
                          #    2   7
    def insertarElemento(self,pos1,nuevo):
        print("Dato insertado: ",self.lista.insert(pos1,nuevo))
        
        #[2,4,6,8,10] = [2,4,7,6,8,10] 
        # 0 1 2 3 4
        
    def mostrar(self):
        if len(self.lista)==0:
            print("*"*20,"Lista Vacia","*"*20)
        else:
            print("*"*20,"Lista de Datos","*"*20)
            for i  in self.lista:
                print(i)
    
    def buscar(self,valor):
        print("La posicion del dato buscado es: ",self.lista.index(valor))

    

    

