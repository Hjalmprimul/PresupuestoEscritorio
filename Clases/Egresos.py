from tkinter import messagebox
from ConexionDB import ConexionDB

class Egreso():
    def __init__(self,id = 0, descripcion = "",fecha = "", monto = 0):
        self.id = id
        self.descripcion = descripcion
        self.fecha = fecha
        self.monto = monto
    
    def Agregar(self):
        conexDB = ConexionDB()
        sql = "insert into egresos(Descripcion,Fecha,Monto) values ('%s', '%s', '%s')"
        conexDB.cursor.execute(sql %(self.descripcion,self.fecha,self.monto))
        conexDB.con.commit
        messagebox.showinfo('Agregar','Egreso de: $'+str(self.monto)+' agregado.')
        conexDB.cerrar()
        
    def ListaEgresos():
        conexDB = ConexionDB()
        sql = "select * from Egresos order by id desc"
        conexDB.cursor.execute(sql)
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos

    def Eliminar(self):
        conexDB = ConexionDB()
        sql = "delete from egresos where id=%s"
        try:
            conexDB.cursor.execute(sql %self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar','Egreso Eliminado!')
        except:
            messagebox.showerror('Eliminar','No se ha seleccionado ningun Egreso.')

    def Editar(self):
        conexDB = ConexionDB()
        sql = "update egresos set Descripcion='%s', Fecha='%s', Monto='%s' where id='%s'"
        conexDB.cursor.execute(sql %(self.descripcion, self.fecha, self.monto, self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar','Datos del Egreso Modificados')
        conexDB.cerrar()
    
    def buscarFecha(self):
        conexDB = ConexionDB()
        fecha = '%' + str(self.fecha) + '%'
        sql = "select * from egresos where fecha like '%s'"
        conexDB.cursor.execute(sql %(fecha))
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos

    def buscar(self):
        conexDB = ConexionDB()
        fecha = '%' + str(self.fecha) + '%'
        desc = '%' + str(self.descripcion) + '%'
        sql = "select * from egresos where fecha like '%s' and descripcion like '%s'"
        conexDB.cursor.execute(sql %(fecha,desc))
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos