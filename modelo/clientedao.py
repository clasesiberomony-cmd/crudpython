from modelo.cliente import Cliente
from modelo.conexionbd import ConexionBD
class ClienteDAO():
    def __init__(self):
        self.bd = ConexionBD()#acceder a la conexion
        self.cliente = Cliente()#acceder a la clase producto
    
    def listarClientes(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexión
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_clientes]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()
    
    def guardarCliente(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        sp = "exec [dbo].[sp_insertar_cliente] @nombre=?,@correo=?,@fechaRegistro=?,"
        param = (self.cliente.nombre,self.cliente.correo,self.cliente.fechaRegistro)
        cursor = self.bd.conexion.cursor()
        cursor.excecute(sp,param)
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexion()
    
    def actualizarCliente(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        sp = "exec [dbo].[sp_actualizar_cliente] @id_cliente=?,@nombre=?,@correo=?,@fechaRegistro=?,"
        param = (self.cliente.id_cliente,self.cliente.nombre,self.cliente.correo,self.cliente.fechaRegistro)
        cursor = self.bd.conexion.cursor()
        cursor.excecute(sp,param)
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexion()
    
    def eliminarCliente(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        sp = "exec [dbo].[sp_eliminar_cliente] @id_cliente=?"
        param = (self.cliente.id_cliente)
        cursor = self.bd.conexion.cursor()
        cursor.excecute(sp,param)
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexion()
    
    def contarClientes(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        funcion = "select [dbo].[fn_contar_clientes]()"
        cursor = self.bd.conexion.cursor()
        cursor.excecute(funcion)
        cantidad = cursor.fetchone()
        print(cantidad[0])
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexion()