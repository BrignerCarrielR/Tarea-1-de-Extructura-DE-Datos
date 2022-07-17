
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
    def __init__(self,codigo,nombre,descripcion):
        self.codigo=codigo
        self.nombre=nombre
        self.accion=descripcion
    def mostrarRol(self):
        print('Cod Rol: {}            Rol: {} '.format(self.codigo, self.nombre) )

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
rol1=Rol('2','Estudiante','recibir clases')
rol1.mostrarRol()
opcion1=OpcionesSistema('1','Aula Virtual','**')
opcion1.mostrarSistema()
operaciones1=OperacionesOpciones('3','Enviar tarea','**')
operaciones1.mostrarOperaciones()
print()