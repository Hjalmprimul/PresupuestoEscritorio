from ConexionDB import ConexionDB

class Balance():
    def __init__(self, mes, monto):
        self.mes = mes
        self.monto = monto

    def verificar(self,egreOingre):
        conexDB = ConexionDB()
        sql = "select * from balances where mes='%s'"
        conexDB.cursor.execute(sql %(self.mes))
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        if len(datos) == 0:
            self.Nuevo(egreOingre)
        else:
            self.Actualizar(egreOingre)
    
    def Nuevo(self, egreOingre):
        conexDB = ConexionDB()
        sql = "insert into balances(mes, monto) values ('%s','%s')"
        if egreOingre == 0:
            conexDB.cursor.execute(sql %(self.mes, self.monto))
        elif egreOingre == 1:
            conexDB.cursor.execute(sql %(self.mes, (0-self.monto)))
        conexDB.con.commit
        conexDB.cerrar()

    def Actualizar(self,egreOingre):
        conexDB = ConexionDB()
        sql = "select monto from balances where mes='%s'"
        conexDB.cursor.execute(sql %(self.mes))
        dato = conexDB.cursor.fetchall()[0][0]
        sql = "update balances set monto='%s' where mes='%s'"
        if egreOingre == 0:
            conexDB.cursor.execute(sql %((dato+self.monto),self.mes))
        elif egreOingre == 1:
            conexDB.cursor.execute(sql %((dato-self.monto),self.mes))
        conexDB.con.commit
        conexDB.cerrar()