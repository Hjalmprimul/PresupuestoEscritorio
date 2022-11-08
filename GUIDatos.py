from tkinter import *
from tkinter import messagebox, ttk
from Clases.Balances import Balance

class interfaceDatos (Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root=root
        self.pack()
        self.variableMes = StringVar()
        self.variableMes.set('Seleccionar Mes')
        self.variableAño = StringVar()
        self.variableAño.set('Seleccionar Año')
        self.datos = Balance.listarBalances()
        self.gui()

    def gui (self):
        self.config(bg='thistle2')

        self.tituloMarco = Label(self, text='BALANCES')
        self.tituloMarco.grid(row=0, column=0,columnspan=4, padx=10, pady=10)
        self.tituloMarco.config(bg="thistle2", font=("Georgia", 16, "bold"))

        self.mes = OptionMenu(self, self.variableMes,'01-Enero','02-Febrero','03-Marzo','04-Abril','05-Mayo','06-Junio','07-Julio','08-Agosto','09-Septiembre','10-Octubre','11-Noviembre','12-Diciembre')
        self.mes.grid(row=1,column=0,padx=10 ,sticky='w')
        self.mes.config(width=16, font=("Georgia", 10), cursor='hand2')

        self.año = OptionMenu(self, self.variableAño, *self.AñosPosibles(self.datos))
        self.año.grid(row=1,column=1,padx=10)
        self.año.config(width=12, font=("Georgia", 10), cursor='hand2')

        self.buscar= Button(self, text="Buscar", command=lambda:self.Mostrar())
        self.buscar.grid(row=1,column=3,sticky='e', padx=10)
        self.buscar.config(bg='#F5967C', font=("Georgia", 10), cursor='hand2')

        self.todos= Button(self, text="Ver Todos", command=lambda:self.VerTodos(self.datos))
        self.todos.grid(row=2,column=0,columnspan=4,padx=10,pady=10)
        self.todos.config(bg='#A3F57C',width=45 ,font=("Georgia", 10), cursor='hand2')

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.balanceTV = ttk.Treeview(self, columns=('#1'))
        self.balanceTV.grid(row=3, column=0, columnspan=4, sticky='w', pady=10)

        self.balanceScroll = ttk.Scrollbar(self, orient='vertical', command=self.balanceTV.yview)
        self.balanceScroll.grid(row=3, column=3, sticky='nsw',pady=10)
        self.balanceTV.configure(yscrollcommand=self.balanceScroll.set)

        self.balanceTV.heading('#0', text='Mes')
        self.balanceTV.column('#0', width=300)
        self.balanceTV.heading('#1', text='Balance')
        self.balanceTV.column('#1', width=70)

        self.VerTodos(self.datos)

    def ConversorFecha(self, dato):
        st = ''
        if dato == '01':
            st = 'Enero'
        elif dato == '02':
            st = 'Febrero'
        elif dato == '03':
            st = 'Marzo'
        elif dato == '04':
            st = 'Abril'
        elif dato == '05':
            st = 'Mayo'
        elif dato == '06':
            st = 'Junio'
        elif dato == '07':
            st = 'Julio'
        elif dato == '08':
            st = 'Agosto'
        elif dato == '09':
            st = 'Septiembre'
        elif dato == '10':
            st = 'Octubre'
        elif dato == '11':
            st = 'Noviembre'
        elif dato == '12':
            st = 'Diciembre'
        return st

    def StringPeso (self, dato):
        st = ''
        pres = int(dato)

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
    
    def VerTodos(self, datos): 
        self.vaciar()     
        for i in range(0,len(datos)):
            st = self.ConversorFecha(datos[i][0][:-5]) + ' de ' + datos[i][0][3:] + ':'
            if datos[i][1] < 0:
                color = 'rojo'
            else:
                color = 'verde'
            self.balanceTV.insert('',0, text= st,values=(self.StringPeso(datos[i][1])), tags=color)
        self.balanceTV.tag_configure("rojo", background='#F5967C')
        self.balanceTV.tag_configure("verde", background='#A3F57C')

    def AñosPosibles(self, datos):
        list = []
        for i in range(0,len(datos)):
            if datos[i][0][3:] in list:
                pass
            else:
                list.append(datos[i][0][3:])
        return list
    
    def Mostrar(self):
        if self.variableMes.get() != 'Seleccionar Mes' or self.variableAño.get() != 'Seleccionar Año':
            mes = self.variableMes.get()[0:2]
            año = self.variableAño.get()
            balance = Balance(mes+'/'+año,0)
            dato = balance.listarEspecifico()
            self.VerTodos(dato)
        else:
            messagebox.showerror("ERROR","No seleccionaste mes o año.")
    
    def vaciar(self):
        filas = self.balanceTV.get_children()
        for i in filas:
            self.balanceTV.delete(i)