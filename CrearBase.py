import sqlite3

miConex = sqlite3.connect("Base de Datos/Base.db")
miCursor = miConex.cursor()

miCursor.execute("""CREATE TABLE INGRESOS (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                DESCRIPCION VARCHAR(50),
                MONTO INTEGER,
                FECHA VARCHAR(11))""")

miCursor.execute("""CREATE TABLE EGRESOS (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                DESCRIPCION VARCHAR(50),
                MONTO INTEGER,
                FECHA VARCHAR(11))""")

miCursor.execute("""CREATE TABLE BALANCES (
                MES VARCHAR NOT NULL PRIMARY KEY,
                MONTO INTERGER)""")

miConex.close()