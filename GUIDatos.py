import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
from Clases.Egresos import Egreso
from Clases.Ingresos import Ingreso
import re

class interfaceDatos (Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root=root
        self.pack()

    def gui (self):
        self.config(bg='thistle2')