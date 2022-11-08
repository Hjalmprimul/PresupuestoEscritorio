from tkinter import *
from tkinter import messagebox, ttk
from Clases.Ingresos import Ingreso
from Clases.Egresos import Egreso


class interfaceConsultas (Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        global añoVariable, mesVariable, diaVariable, descVariable, guia
        descVariable = StringVar()
        añoVariable = StringVar()
        mesVariable = StringVar()
        diaVariable = StringVar()
        guia = 'Buscar datos por Descripción, por Año,\n por Mes+Año y por Dia+Mes+Año'
        self.gui()

    def gui (self):
        self.config(bg='thistle2')

        self.titulo = Label(self, text='CONSULTAS')
        self.titulo.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        self.titulo.config(bg='thistle2', font=("Georgia", 16, "bold"))

        self.guia = Label(self, text= guia)
        self.guia.grid(row=1,column=0,columnspan=4,padx=10,pady=10)
        self.guia.config(bg='thistle2', font=("Georgia", 8))

        self.añoTxt = Label(self, text='Por Año:')
        self.añoTxt.grid(row=2,column=0,padx=30,pady=10)
        self.añoTxt.config(bg='thistle2', font=("Georgia", 10))

        self.mesTxt = Label(self, text='Por Mes:')
        self.mesTxt.grid(row=3,column=0,padx=30,pady=10)
        self.mesTxt.config(bg='thistle2', font=("Georgia", 10))

        self.diaTxt = Label(self, text='Por Dia:')
        self.diaTxt.grid(row=4,column=0,padx=30,pady=10)
        self.diaTxt.config(bg='thistle2', font=("Georgia", 10))

        self.descTxt = Label(self, text='Por Desc:')
        self.descTxt.grid(row=5,column=0,padx=30,pady=10)
        self.descTxt.config(bg='thistle2', font=("Georgia", 10))

        self.añoEntry = Entry(self,textvariable=añoVariable)
        self.añoEntry.grid(row=2, column=2, padx=30, pady=10, sticky="w")
        self.añoEntry.config(bg="white", width=10, font=("Georgia", 12))

        self.mesEntry = Entry(self,textvariable=mesVariable)
        self.mesEntry.grid(row=3, column=2, padx=30, pady=10, sticky="w")
        self.mesEntry.config(bg="white", width=10, font=("Georgia", 12))

        self.diaEntry = Entry(self,textvariable=diaVariable)
        self.diaEntry.grid(row=4, column=2, padx=30, pady=10, sticky="w")
        self.diaEntry.config(bg="white", width=10, font=("Georgia", 12))

        self.descEntry = Entry(self,textvariable=descVariable)
        self.descEntry.grid(row=5, column=2, padx=30, pady=10, sticky="w")
        self.descEntry.config(bg="white", width=10, font=("Georgia", 12))

        self.buscar= Button(self, text="Buscar", command=lambda:self.Buscar())
        self.buscar.grid(row=6, column=0, columnspan=3, pady=10, padx=30)
        self.buscar.config(bg='dark green' ,width=25, font=("Georgia", 12), cursor='hand2')

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.datosTV = ttk.Treeview(self, columns=('Monto','Fecha'))
        self.datosTV.grid(row=7, column=0, columnspan=3, sticky='w')

        self.datosScroll = ttk.Scrollbar(self, orient='vertical', command=self.datosTV.yview)
        self.datosScroll.grid(row=7, column=43, sticky='nsw')
        self.datosTV.configure(yscrollcommand=self.datosScroll.set)

        self.datosTV.heading('#0', text='Descripción')
        self.datosTV.column('#0', width=130)
        self.datosTV.heading('#1', text='Monto')
        self.datosTV.column('#1', width=65)
        self.datosTV.heading('#2', text='Fecha')
        self.datosTV.column('#2', width=75)
    
    def Buscar(self):
        if descVariable.get() == '':
            if añoVariable.get() == '':
                messagebox.showerror("ERROR","No se han seleccionado datos de Año y Descripcion.")
            else:
                if mesVariable.get() == '':
                    st = añoVariable.get()
                else:
                    if diaVariable.get() == '':
                        st = mesVariable.get() + '/' + añoVariable.get()
                    else:
                        st = diaVariable.get() + '/' + mesVariable.get() + '/' + añoVariable.get()
                ingre = Ingreso(0,'',st,0)
                egre = Egreso(0,'',st,0)
                datosI = ingre.buscarFecha()
                datosE = egre.buscarFecha()
        elif añoVariable.get() == '':
            desc = descVariable.get()
            ingre = Ingreso(0,desc,'',0)
            egre = Egreso(0,desc,'',0)
            datosI = ingre.buscar()
            datosE = egre.buscar()
        else:
            if mesVariable.get() == '':
                desc = descVariable.get()
                st = añoVariable.get()
            else:
                if diaVariable.get() == '':
                    desc = descVariable.get()
                    st = mesVariable.get() + '/' + añoVariable.get()
                else:
                    desc = descVariable.get()
                    st = diaVariable.get() + '/' + mesVariable.get() + '/' + añoVariable.get()
            ingre = Ingreso(0,desc,st,0)
            egre = Egreso(0,desc,st,0)
            datosI = ingre.buscar()
            datosE = egre.buscar()
        self.llenar(datosI, datosE)
        self.resetEntrys()

    def llenar(self,datosI, datosE):
        self.vaciar()
        for d in datosI:
            self.datosTV.insert('',0,text=d[1],values=('$'+ str(d[2]),d[3]), tags='green')
        for d in datosE:
            self.datosTV.insert('',0,text=d[1],values=('-$' + str(d[2]),d[3]), tags='red')
        self.datosTV.tag_configure("red", background='#F5967C')
        self.datosTV.tag_configure("green", background='#A3F57C')

    def vaciar(self):
        filas = self.datosTV.get_children()
        for f in filas:
            self.datosTV.delete(f)

    def resetEntrys(self):
        descVariable.set('')
        añoVariable.set('')
        mesVariable.set('')
        diaVariable.set('')