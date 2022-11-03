import sqlite3

class ConexionDB:
    def __init__(self) -> None:
        self.con = sqlite3.connect("Base de Datos/Base.db")
        self.cursor = self.con.cursor()
    
    def cerrar(self):
        self.con.commit()
        self.con.close()
