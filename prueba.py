import tkinter as tk
from tkinter import messagebox

# Funciones para las opciones del menú
def nueva_archivo():
    messagebox.showinfo("Nuevo Archivo", "Has seleccionado Nuevo Archivo")

def abrir_archivo():
    messagebox.showinfo("Abrir Archivo", "Has seleccionado Abrir Archivo")

def guardar_archivo():
    messagebox.showinfo("Guardar Archivo", "Has seleccionado Guardar Archivo")

def salir():
    ventana.quit()

def cortar():
    messagebox.showinfo("Cortar", "Has seleccionado Cortar")

def copiar():
    messagebox.showinfo("Copiar", "Has seleccionado Copiar")

def pegar():
    messagebox.showinfo("Pegar", "Has seleccionado Pegar")

def acerca_de():
    messagebox.showinfo("Acerca de", "Este es un menú de ejemplo creado con Tkinter")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Menú Bar")
ventana.geometry("400x300")

# Crear el menú bar
menu_bar = tk.Menu(ventana)

# Crear el menú Archivo
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nueva_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

# Crear el menú Editar
menu_editar = tk.Menu(menu_bar, tearoff=0)
menu_editar.add_command(label="Cortar", command=cortar)
menu_editar.add_command(label="Copiar", command=copiar)
menu_editar.add_command(label="Pegar", command=pegar)

menu_bar.add_cascade(label="Editar", menu=menu_editar)

# Crear el menú Ayuda
menu_ayuda = tk.Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)

menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

# Añadir el menú bar a la ventana
ventana.config(menu=menu_bar)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
