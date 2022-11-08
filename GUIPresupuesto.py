import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
from Clases.Egresos import Egreso
from Clases.Ingresos import Ingreso
from Clases.Balances import Balance
import re

class interfacePresupuesto (Frame):
    # INICIADOR
    def __init__(self, root=None):
        super().__init__(root)
        self.root=root
        self.pack()
        global Descripcion, Fecha, Monto, FechaRegex, txt, col
        Descripcion = StringVar()
        Fecha = StringVar()
        Monto = IntVar()
        FechaRegex = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
        # PRESUPUESTO
        txt = self.StringPeso(self.CalculoPresupuesto())
        col = ''
        if txt[0] == '-':
            col = 'red2'
        else:
            col = 'dark green'
        self.gui()
    # Objetos Interfaz
    def gui (self):
        self.config(bg='thistle2')

        # TITULO
        self.tituloMarco = Label(self, text= "PRESUPUESTO")
        self.tituloMarco.grid(row=0, column=3 ,pady=10, padx=10)
        self.tituloMarco.config(bg="thistle2", font=("Georgia", 16, "bold"))
        
        # PRESUPUESTO
        self.presupuesto = Label(self, text = txt)
        self.presupuesto.grid(row=1, column=3, padx=10, pady=10)
        self.presupuesto.config(bg="thistle2", font=("Arial", 16, "bold"), anchor="center", fg=col)

        # LABELS
        self.lab1=Label(self, text= "Descripción: ")
        self.lab1.grid(row=2, column=1, columnspan=2 ,padx=1, pady=10)
        self.lab1.config(bg= "thistle2", width=15, font=("Georgia", 12), anchor="w")

        self.lab2=Label(self, text= "Monto: ")
        self.lab2.grid(row=3, column=1, columnspan=2 ,padx=1, pady=10)
        self.lab2.config(bg= "thistle2", width=15, font=("Georgia", 12), anchor="w")


        self.lab3=Label(self, text= "Fecha: ")
        self.lab3.grid(row=4, column=1, columnspan=2 ,padx=1, pady=10)
        self.lab3.config(bg= "thistle2", font=("Georgia", 12), width=15, anchor="w")

        # ENTRYS
        self.txtDesc = Entry(self,textvariable=Descripcion)
        self.txtDesc.grid(row=2, column=3, padx=10, pady=10, columnspan=3, sticky="w")
        self.txtDesc.config(bg="white", width=30, font=("Georgia", 12))

        self.txtMonto = Entry(self,textvariable=Monto)
        self.txtMonto.grid(row=3, column=3, padx=10, pady=10, columnspan=3, sticky="w")
        self.txtMonto.config(bg="white", font=("Georgia", 12), width=15)

        self.txtFecha = Entry(self,textvariable=Fecha)
        self.txtFecha.grid(row=4, column=3, padx=10, pady=10, columnspan=3, sticky="w")
        self.txtFecha.config(bg="white", font=("Georgia", 12), width=15)

        # BOTONES
        self.botonIngreso= Button(self, text="Guardar Ingreso", command=lambda:self.Guardar(0))
        self.botonIngreso.grid(row=5, column=1, columnspan=2, pady=10, padx=10, sticky="w")
        self.botonIngreso.config(bg='dark green' ,width=20, font=("Georgia", 12), cursor='hand2')

        self.botonEgreso= Button(self, text="Guardar Egreso", command=lambda:self.Guardar(1))
        self.botonEgreso.grid(row=5, column=3, columnspan=2, pady=10, padx=10, sticky="w")
        self.botonEgreso.config(bg='red3',width=20, font=("Georgia", 12), cursor='hand2')

        self.botonSalir= Button(self, text="Salir", command=lambda:self.salir())
        self.botonSalir.grid(row=5, column=5, pady=10, padx=10, sticky="w")
        self.botonSalir.config(width=10, font=("Georgia", 12), cursor='hand2')

        # Titulos TreeView
        self.lab4=Label(self, text= "Ingresos")
        self.lab4.grid(row=6, column=1,padx=1, pady=10)
        self.lab4.config(bg= "thistle2",font=("Georgia", 12), fg="dark green")

        self.lab5=Label(self, text= "Egresos")
        self.lab5.grid(row=6, column=5,padx=1, pady=10, sticky="e")
        self.lab5.config(bg= "thistle2",font=("Georgia", 12), fg="red2")

        # TreeView Ingresos
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.IngreTV = ttk.Treeview(self, columns=('Monto','Fecha'))
        self.IngreTV.grid(row=7, column=0, columnspan=3, sticky='w')

        self.IngreScroll = ttk.Scrollbar(self, orient='vertical', command=self.IngreTV.yview)
        self.IngreScroll.grid(row=7, column=3, sticky='nsw')
        self.IngreTV.configure(yscrollcommand=self.IngreScroll.set)

        self.IngreTV.heading('#0', text='Descripción')
        self.IngreTV.column('#0', width=130)
        self.IngreTV.heading('#1', text='Monto')
        self.IngreTV.column('#1', width=65)
        self.IngreTV.heading('#2', text='Fecha')
        self.IngreTV.column('#2', width=75)

        # TreeView Egresos
        self.EgreTV = ttk.Treeview(self, columns=('Monto','Fecha'))
        self.EgreTV.grid(row=7, column=5, columnspan=3, sticky='w')

        self.EgreScroll = ttk.Scrollbar(self, orient='vertical', command=self.EgreTV.yview)
        self.EgreScroll.grid(row=7, column=4, sticky='nse')
        self.EgreTV.configure(yscrollcommand=self.EgreScroll.set)

        self.EgreTV.heading('#0', text='Descripción')
        self.EgreTV.column('#0', width=130)
        self.EgreTV.heading('#1', text='Monto')
        self.EgreTV.column('#1', width=65)
        self.EgreTV.heading('#2', text='Fecha')
        self.EgreTV.column('#2', width=75)

        # BOTONES DE EDICION Y ELIMINACION
        self.EditarIngreso= Button(self, text="Editar", command=lambda:self.Editar(0))
        self.EditarIngreso.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="w")
        self.EditarIngreso.config(bg='dark green', width=10, font=("Georgia", 12), cursor='hand2')

        self.EliminarIngreso= Button(self, text="Eliminar", command=lambda:self.Eliminar(0))
        self.EliminarIngreso.grid(row=8, column=1, columnspan=2,  pady=10, padx=10, sticky="e")
        self.EliminarIngreso.config(bg='dark green' ,width=10, font=("Georgia", 12), cursor='hand2')

        self.EditarEgreso= Button(self, text="Editar", command=lambda:self.Editar(1))
        self.EditarEgreso.grid(row=8, column=6, columnspan=2, pady=10, padx=10, sticky="w")
        self.EditarEgreso.config(bg='red2' ,width=10, font=("Georgia", 12), cursor='hand2')

        self.EliminarEgreso= Button(self, text="Eliminar", command=lambda:self.Eliminar(1))
        self.EliminarEgreso.grid(row=8, column=5, columnspan=2, pady=10, padx=10, sticky="w")
        self.EliminarEgreso.config(bg='red2' ,width=10, font=("Georgia", 12), cursor='hand2')
        self.Llenar()
    # Calculo Numerico de Presupuesto
    def CalculoPresupuesto(self):
        presupuesto = 0
        egreTotal = 0
        ingreTotal = 0
        
        miConex = sqlite3.connect("Base de Datos/Base.db")
        miCursor = miConex.cursor()

        miCursor.execute("SELECT MONTO FROM EGRESOS")
        datosEgreso = miCursor.fetchall()
        for dato in datosEgreso:
            egreTotal = egreTotal + dato[0]

        miCursor.execute("SELECT MONTO FROM INGRESOS")
        datosIngreso = miCursor.fetchall()
        for dato in datosIngreso:
            ingreTotal = ingreTotal + dato[0]

        miConex.close()

        presupuesto = ingreTotal - egreTotal

        return presupuesto
    # Modificacion String Peso
    def StringPeso (self,numero):
        st = ''
        pres = numero

        if pres < 0:
            presST = str(pres)[1:]
            presST = presST[::-1]
            i = 0
            for char in presST:
                i = i + 1
                st = char + st
                if i % 3 == 0 and i != len(presST):
                    st = '.' + st
            st = '-$' + st

        elif pres > 0:
            x = 0
            presST = str(pres)[::-1]
            for char in presST:
                x = x + 1
                st = char + st
                if x % 3 == 0 and x != len(presST):
                    st = '.' + st
            st = '$' + st

        else:
            st = "$" + str(pres)

        return st
    # Guardar Ingreso y Egreso
    def Guardar(self,egreOingre):
        # Error por datos mal cargados
        if Descripcion.get()=='' or Monto.get()==0 or Fecha.get()=='':
            messagebox.showerror("ERROR", "Alguna de las entradas esta vacia")
        elif re.fullmatch(FechaRegex, Fecha.get())==None:
            messagebox.showerror("ERROR", "La fecha esta mal")
        else:
            if egreOingre == 0:
                if esNuevo:
                    nIngreso = Ingreso(0,Descripcion.get(),Fecha.get(),Monto.get())
                    nIngreso.Agregar()
                    self.VerifBalanceGuardar(0)
                else:
                    nIngreso = Ingreso(self.IngreTV.item(self.IngreTV.selection())['tags'][0],Descripcion.get(),Fecha.get(),Monto.get())
                    nIngreso.Editar()
                    self.VerifBalanceEditar(0)
                self.ResetEntrys()
                self.Llenar()
            elif egreOingre == 1:
                if esNuevo:
                    nEgreso = Egreso(0,Descripcion.get(),Fecha.get(),Monto.get())
                    nEgreso.Agregar()
                    self.VerifBalanceGuardar(1)
                else:
                    nEgreso = Egreso(self.EgreTV.item(self.EgreTV.selection())['tags'][0],Descripcion.get(),Fecha.get(),Monto.get())
                    nEgreso.Editar()
                    self.VerifBalanceEditar(1)
                self.ResetEntrys()
                self.Llenar()
    # Cerrar Ventana
    def salir(self):
        respuesta = messagebox.askquestion("Salir", "Confirma que quieres salir?")
        if respuesta == "yes":
            self.root.destroy()
    # Resetear HUB
    def ResetEntrys(self):
        Descripcion.set("")
        Monto.set(0)
        Fecha.set("")

        self.botonEgreso.config(state='normal')
        self.botonIngreso.config(state='normal')
        self.EliminarEgreso.config(state='normal')
        self.EliminarIngreso.config(state='normal')
        self.EditarEgreso.config(state='normal')
        self.EditarIngreso.config(state='normal')

        txt = self.StringPeso(self.CalculoPresupuesto())
        self.presupuesto.config(text= txt)

        if txt[0] == '-':
            self.presupuesto.config(fg="red2")
        else:
            self.presupuesto.config(fg="dark green")
    # Vaciar TreeViews
    def vaciar(self):
        filas = self.IngreTV.get_children()
        for f in filas:
            self.IngreTV.delete(f)
        filas = self.EgreTV.get_children()
        for f in filas:
            self.EgreTV.delete(f)
    # Llenar TreeViews
    def Llenar(self):
        self.vaciar()
        global esNuevo
        esNuevo = True
        
        datos = Ingreso.ListaIngresos()
        for d in datos:
            self.IngreTV.insert('', 0, text=d[1],values=(self.StringPeso(d[2]),d[3]), tags=d[0])
        
        datos = Egreso.ListaEgresos()
        for d in datos:
            self.EgreTV.insert('', 0, text=d[1], values=(self.StringPeso(d[2]),d[3]), tags=d[0])
    # Editar Ingreso y Egreso
    def Editar(self,egreOingre):
        global esNuevo, montoAnterior, fechaAnterior
        esNuevo = False
        if egreOingre == 0:
            try:
                self.ResetEntrys()
                #SET VARIABLES
                Descripcion.set(self.IngreTV.item(self.IngreTV.selection())['text'])
                monto = (self.IngreTV.item(self.IngreTV.selection())['values'][0])
                st = ''
                for char in monto:
                    if char != '$' and char != '.':
                        st = st + char
                montoAnterior = st
                Monto.set(st)
                fechaAnterior = self.IngreTV.item(self.IngreTV.selection())['values'][1]
                Fecha.set(self.IngreTV.item(self.IngreTV.selection())['values'][1])
                #ESTADO BOTONES
                self.botonEgreso.config(state="disable")
                self.EliminarEgreso.config(state="disable")
                self.EditarEgreso.config(state="disable")
            except:
                messagebox.showerror('Editar','No se ha seleccionado ningun Ingreso')
        else:
            try:
                self.ResetEntrys()
                #SET VARIABLES
                Descripcion.set(self.EgreTV.item(self.EgreTV.selection())['text'])
                monto = self.EgreTV.item(self.EgreTV.selection())['values'][0]
                st = ''
                for char in monto:
                    if char != '$' and char != '.':
                        st = st + char
                montoAnterior = st
                Monto.set(st)
                fechaAnterior = self.EgreTV.item(self.EgreTV.selection())['values'][1]
                Fecha.set(self.EgreTV.item(self.EgreTV.selection())['values'][1])
                #ESTADO BOTONES
                self.botonIngreso.config(state="disable")
                self.EliminarIngreso.config(state="disable")
                self.EditarIngreso.config(state="disable")
            except:
                messagebox.showerror('Editar','No se ha seleccionado ningun Egreso')
        self.txtDesc.focus()
    # Eliminar Ingreso y Egreso
    def Eliminar(self,egreOingre):
        if egreOingre == 0:
            ingre = Ingreso(self.IngreTV.item(self.IngreTV.selection())['tags'][0],"","",self.IngreTV.item(self.IngreTV.selection())['values'][0])
            ingre.Eliminar()
            self.ResetEntrys()
            self.VerifBalanceEliminar(egreOingre)
        else:
            egre = Egreso(self.EgreTV.item(self.EgreTV.selection())['tags'][0])
            egre.Eliminar()
            self.ResetEntrys()
            self.VerifBalanceEliminar(egreOingre)
        self.Llenar()
    # Verifica, crea balance y actualiza balance
    def VerifBalanceGuardar(self,egreOingre):
        mes = Fecha.get()[3:]
        balance = Balance(mes,Monto.get())
        balance.verificar(egreOingre)
    def VerifBalanceEliminar(self,egreOingre):
        if egreOingre == 0:
            mes = self.IngreTV.item(self.IngreTV.selection())['values'][1]
            monto = self.IngreTV.item(self.IngreTV.selection())['values'][0]
            st = ''
            for char in monto:
                if char != '$' and char != '.':
                    st = st + char
        elif egreOingre == 1:
            mes = self.EgreTV.item(self.EgreTV.selection())['values'][1]
            monto = self.EgreTV.item(self.EgreTV.selection())['values'][0]
            st = ''
            for char in monto:
                if char != '$' and char != '.':
                    st = st + char
            st = '-' + st
        balance = Balance(mes[3:],int(st))
        balance.verificar(1)
    def VerifBalanceEditar(self,egreOingre):
        if fechaAnterior == Fecha.get():
            balance = Balance(Fecha.get()[3:],int(montoAnterior)-int(Monto.get()))
            balance.verificar(0)
        else:
            if montoAnterior == Monto.get():
                balance = Balance(fechaAnterior[3:],Monto.get())
                balance2 = Balance(Fecha.get()[3:],Monto.get())
            else:
                balance = Balance(fechaAnterior[3:],montoAnterior)
                balance2 = Balance(Fecha.get()[3:],Monto.get())
            if egreOingre == 0:
                balance.verificar(1)
                balance2.verificar(0)
            else:
                balance.verificar(0)
                balance2.verificar(1)