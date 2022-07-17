class Usuario:
    def __init__(self,cedula,nombre,clave,correo,telefono):
        self.cedula=cedula
        self.usuario=nombre
        self.correo=correo
        self.clave=clave
        self.telefono=telefono
    def mostrarUsuario(self):
        print('Cedula: {}    Nombre: {} '.format(self.cedula, self.usuario) )

class Rol:
    def opcionRol(self):
        # Imprimimos el menú en pantalla
        print("""
            1) Estudiante       3) Administrador
            2) Docente        
            """)

        # Leemos lo que ingresa el usuario
        eligio=input("-Selecciona algo :")

        # Según lo que ingresó, código diferente
        if eligio=="1" or eligio=="Estudiante":
            print("Codigo 1         Rol: Estudinte")
        elif eligio=="2":
            print("Codigo 2         Rol: Docente")
        elif eligio=="3":
            print("Codigo 3         Rol: Administrador")
        else:
            print("Opción no válida")
    
    def mostrarRol(self):
        # print('Cod Rol: {}            Rol: {} '.format(self.codigo, self.nombre) )
        pass

class OpcionesSistema:
    def __init__(self,codigoOpc,nombre,accion):
        self.codigo=codigoOpc
        self.nombre=nombre
        self.descripcion=accion
    def mostrarSistema(self):
        print('Cod Opc: {}            Opciones: {} '.format(self.codigo, self.nombre) )

class OperacionesOpciones:
    def __init__(self,codigoOpe,nombre,accion):
        self.codigo=codigoOpe
        self.nombre=nombre
        self.descripcion=accion       
    def mostrarOperaciones(self):
        print('Cod Ope: {}            Operaciones: {} '.format(self.codigo, self.nombre) )

print()
usuario1=Usuario('0987654321','Brigner ','298163','bacr','0960285305')
usuario1.mostrarUsuario()
rol1=Rol()
rol1.opcionRol()
rol1.mostrarRol()
opcion1=OpcionesSistema('1','Aula Virtual','**')
opcion1.mostrarSistema()
operaciones1=OperacionesOpciones('3','Enviar tarea','**')
operaciones1.mostrarOperaciones()
print()