from tkinter import *
from GUIPresupuesto import interfacePresupuesto
from GUIDatos import interfaceDatos
from GUIConsultas import interfaceConsultas

def Presupuesto(root):
    ventana = Toplevel(root)
    ventana.title('Gestion de Presupuesto')
    ventana.transient(root)
    app = interfacePresupuesto(root=ventana)

def Datos(root):
    ventana = Toplevel(root)
    ventana.title('Informe de Datos')
    ventana.transient(root)
    app = interfaceDatos(root=ventana)
 
def Consultas(root):
    ventana = Toplevel(root)
    ventana.title('Consultas')
    ventana.transient(root)
    app = interfaceConsultas(root=ventana)

def Barra_Menu(root):
    Barra_Menu = Menu(root)
    root.config(menu=Barra_Menu)

    menu_datos = Menu(Barra_Menu,tearoff=0)
    Barra_Menu.add_cascade(label='Funciones',menu=menu_datos)
    menu_datos.add_command(label='Presupuesto',command=lambda:Presupuesto(root))
    menu_datos.add_command(label='Balances Mensuales',command=lambda:Datos(root))
    Barra_Menu.add_cascade(label='Consultar',command=lambda:Consultas(root))
    Barra_Menu.add_cascade(label='Salir',command=lambda:root.destroy())

def main():
    root = Tk()
    root.title('House Business')
    root.resizable(False,False)
    root.geometry('600x400')

    imagen = PhotoImage(file='imagen/Monedas.png')
    background = Label(image= imagen, text='Imagen de fondo')
    background.place(x=0, y=0, relwidth=1, relheight=1)

    Barra_Menu(root)

    root.mainloop()

if __name__ == "__main__":
    main()