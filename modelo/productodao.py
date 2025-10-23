from modelo.producto import Producto
from modelo.conexionbd import ConexionBD
class ProductoDAO():
    def __init__(self):
        self.bd = ConexionBD()#acceder a la conexion
        self.producto = Producto()#acceder a la clase producto
    
    def listarProductos(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexión
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_productos]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()
        #extraer  la información de filas y retornarla a la interfaz grafica
        return filas
    
    def buscarProducto(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexión
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_buscar_producto] @clave=?"
        param =[self.producto.clave]
        cursor.execute(sp,param)
        filas = cursor.fetchall()
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()
        #extraer  la información de filas y retornarla a la interfaz grafica
        return filas
    
    def guardarProducto(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        sp = "exec [dbo].[sp_insertar_producto] @clave=?,@descripcion=?,@existencia=?,@precio=?"
        param = [self.producto.clave,self.producto.descripcion,self.producto.existencia,self.producto.precio]
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp,param)
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()
    
    def actualizarProducto(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        sp = "exec [dbo].[sp_actualizar_producto] @clave=?,@descripcion=?,@existencia=?,@precio=?,"
        param = (self.producto.clave,self.producto.descripcion,self.producto.existencia,self.producto.precio)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp,param)
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()
    
    def eliminarProducto(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        sp = "exec [dbo].[sp_eliminar_producto] @id_producto=?"
        param = (self.producto.id_producto)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp,param)
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()
    
    def contarProducto(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexion
        funcion = "select [dbo].[fn_contar_productos]()"
        cursor = self.bd.conexion.cursor()
        cursor.execute(funcion)
        cantidad = cursor.fetchone()
        print(cantidad[0])
        cursor.commit()
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()