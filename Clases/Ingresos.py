from tkinter import messagebox
from ConexionDB import ConexionDB

class Ingreso():
    def __init__(self,id = 0, descripcion = "",fecha = "", monto = 0):
        self.id = id
        self.descripcion = descripcion
        self.fecha = fecha
        self.monto = monto
    
    def Agregar(self):
        conexDB = ConexionDB()
        sql = "insert into ingresos(Descripcion,Fecha,Monto) values ('%s', '%s', '%s')"
        conexDB.cursor.execute(sql %(self.descripcion,self.fecha,self.monto))
        conexDB.con.commit
        messagebox.showinfo('Agregar','Ingreso de: $'+str(self.monto)+' agregado.')
        conexDB.cerrar()

    def ListaIngresos():
        conexDB = ConexionDB()
        sql = "select * from Ingresos order by id desc"
        conexDB.cursor.execute(sql)
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos

    def Eliminar(self):
        conexDB = ConexionDB()
        sql = "delete from ingresos where id=%s"
        try:
            conexDB.cursor.execute(sql %self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar','Ingreso Eliminado!')
        except:
            messagebox.showerror('Eliminar','No se ha seleccionado ningun Ingreso.')

    def Editar(self):
        conexDB = ConexionDB()
        sql = "update ingresos set Descripcion='%s', Fecha='%s', Monto='%s' where id='%s'"
        conexDB.cursor.execute(sql %(self.descripcion, self.fecha, self.monto, self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar','Datos del Ingreso Modificados')
        conexDB.cerrar()

    def toString(self):
        st = str(self.id) + ' ' + self.descripcion + ' ' + str(self.monto) + ' ' + self.fecha
        return st

    def buscarFecha(self):
        conexDB = ConexionDB()
        fecha = '%' + str(self.fecha) + '%'
        sql = "select * from ingresos where fecha like '%s'"
        conexDB.cursor.execute(sql %(fecha))
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos

    def buscar(self):
        conexDB = ConexionDB()
        fecha = '%' + str(self.fecha) + '%'
        desc = '%' + str(self.descripcion) + '%'
        sql = "select * from ingresos where fecha like '%s' and descripcion like '%s'"
        conexDB.cursor.execute(sql %(fecha, desc))
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos
        