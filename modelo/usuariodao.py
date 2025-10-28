from modelo.usuario import Usuario
from modelo.conexionbd import ConexionBD
class UsuarioDAO():
    def __init__(self):
        self.bd = ConexionBD()#acceder a la conexion
        self.usuario = Usuario()#acceder a la clase 
    
        
    def buscarUsuario(self):
        self.bd.establecerConexionBD()
        #hacemos uso de la conexión
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_buscar_usuario] @nickname=?,@password=?"
        param =[self.usuario.nickname,self.usuario.password]
        print(param)
        cursor.execute(sp,param)
        filas = cursor.fetchall()
        #fin del uso de la base de datos
        self.bd.cerrarConexionBD()
        #extraer  la información de filas y retornarla a la interfaz grafica
        print(filas)
        return filas
    
    